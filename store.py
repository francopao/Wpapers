"""
Persistence layer — JSON-based store for card states, reviews, and user cards.
"""
from __future__ import annotations
import json
from datetime import date, timedelta
from pathlib import Path
from core.srs_engine import CardState

DATA_DIR     = Path("data")
STATES_FILE  = DATA_DIR / "sessions" / "states.json"
REVIEWS_FILE = DATA_DIR / "sessions" / "reviews.json"
UCARDS_FILE  = DATA_DIR / "cards"    / "user_cards.json"


def _load(path: Path) -> dict | list:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        return {} if path.suffix == ".json" and "states" in path.name else []
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return {}


def _save(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


class CardStore:
    # ── States ────────────────────────────────────────────────────────
    def get_state(self, card_id: str) -> CardState:
        states = _load(STATES_FILE)
        if card_id in states:
            return CardState.from_dict(states[card_id])
        return CardState(card_id=card_id)

    def save_state(self, state: CardState):
        states = _load(STATES_FILE)
        states[state.card_id] = state.to_dict()
        _save(STATES_FILE, states)

    def all_states(self) -> dict[str, CardState]:
        raw = _load(STATES_FILE)
        return {cid: CardState.from_dict(d) for cid, d in raw.items()}

    # ── Reviews ───────────────────────────────────────────────────────
    def log_review(self, card_id: str, rating: int, domain: str, topic: str):
        reviews = _load(REVIEWS_FILE)
        if not isinstance(reviews, list):
            reviews = []
        reviews.append({
            "date":    date.today().isoformat(),
            "card_id": card_id,
            "rating":  rating,
            "domain":  domain,
            "topic":   topic,
        })
        _save(REVIEWS_FILE, reviews)

    def all_reviews(self) -> list[dict]:
        r = _load(REVIEWS_FILE)
        return r if isinstance(r, list) else []

    def streak_days(self) -> int:
        reviews = self.all_reviews()
        if not reviews:
            return 0
        days_with_reviews = {r["date"] for r in reviews}
        streak, check = 0, date.today()
        while check.isoformat() in days_with_reviews:
            streak += 1
            check  -= timedelta(days=1)
        return streak

    # ── User cards ────────────────────────────────────────────────────
    def all_user_cards(self) -> list[dict]:
        r = _load(UCARDS_FILE)
        return r if isinstance(r, list) else []

    def save_user_card(self, card: dict):
        cards = self.all_user_cards()
        cards.append(card)
        _save(UCARDS_FILE, cards)
