"""
SM-2 Spaced Repetition Engine — Invest Memoria
Modified SuperMemo SM-2 with Ebbinghaus retention modeling.
"""
from __future__ import annotations
import math
from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from enum import IntEnum


class Rating(IntEnum):
    BLACKOUT  = 0
    WRONG     = 1
    HARD      = 2
    GOOD      = 3
    EASY      = 4
    PERFECT   = 5


@dataclass
class CardState:
    card_id:      str
    ease:         float = 2.5
    interval:     float = 1.0        # days
    repetitions:  int   = 0
    error_count:  int   = 0
    next_review:  str   = ""         # ISO date string
    last_review:  str   = ""
    stability:    float = 1.0        # Ebbinghaus S parameter

    def to_dict(self) -> dict:
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, d: dict) -> "CardState":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


class SRSEngine:
    MIN_EASE = 1.3
    MAX_EASE = 5.0

    def update(self, state: CardState, rating: Rating) -> CardState:
        s = CardState(**state.__dict__)
        s.last_review = date.today().isoformat()

        if rating < Rating.GOOD:
            s.error_count += 1
            s.repetitions  = 0
            s.interval     = 1.0
            s.ease         = max(self.MIN_EASE, s.ease - 0.20)
        else:
            s.repetitions += 1
            if s.repetitions == 1:
                s.interval = 1.0
            elif s.repetitions == 2:
                s.interval = 6.0
            else:
                s.interval = round(s.interval * s.ease, 1)

            delta = {
                Rating.GOOD:    0.0,
                Rating.EASY:   +0.10,
                Rating.PERFECT:+0.15,
            }.get(rating, 0.0)
            s.ease = min(self.MAX_EASE, max(self.MIN_EASE, s.ease + delta))

        # Update Ebbinghaus stability: S grows with each successful review
        if rating >= Rating.GOOD:
            s.stability = s.stability * (1 + 0.2 * rating)
        else:
            s.stability = max(0.5, s.stability * 0.7)

        s.next_review = (date.today() + timedelta(days=max(1, int(s.interval)))).isoformat()
        return s

    def is_due(self, state: CardState) -> bool:
        if not state.next_review:
            return True
        return date.today().isoformat() >= state.next_review

    def days_until_due(self, state: CardState) -> float:
        if not state.next_review:
            return 0.0
        delta = date.fromisoformat(state.next_review) - date.today()
        return max(0.0, delta.days)

    def retention(self, state: CardState) -> float:
        """Ebbinghaus R = e^(-t/S)"""
        if not state.last_review:
            return 0.0
        t = (date.today() - date.fromisoformat(state.last_review)).days
        return math.exp(-t / max(state.stability, 0.1))

    def mastery_score(self, state: CardState) -> float:
        ret = self.retention(state)
        reps_score = min(state.repetitions / 10, 1.0)
        err_penalty = min(state.error_count * 0.05, 0.4)
        return max(0.0, min(1.0, 0.5 * ret + 0.5 * reps_score - err_penalty))
