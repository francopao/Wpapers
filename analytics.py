"""
Analytics engine — mastery metrics, retention curves, topic heatmaps.
"""
from __future__ import annotations
from datetime import date, timedelta
from core.store import CardStore
from core.srs_engine import SRSEngine


class AnalyticsEngine:
    def __init__(self):
        self.store  = CardStore()
        self.engine = SRSEngine()

    def summary(self, all_cards: list[dict]) -> dict:
        states  = self.store.all_states()
        reviews = self.store.all_reviews()

        due_today = sum(
            1 for c in all_cards
            if self.engine.is_due(states.get(c["id"], __import__("core.srs_engine", fromlist=["CardState"]).CardState(card_id=c["id"])))
        )

        masteries = [
            self.engine.mastery_score(states.get(c["id"], __import__("core.srs_engine", fromlist=["CardState"]).CardState(card_id=c["id"])))
            for c in all_cards
        ]
        mean_mastery = sum(masteries) / max(len(masteries), 1)

        rated = [r for r in reviews if r.get("rating") is not None]
        good  = [r for r in rated  if r.get("rating", 0) >= 3]
        accuracy = len(good) / max(len(rated), 1)

        return {
            "due_today":    due_today,
            "mean_mastery": mean_mastery,
            "accuracy":     accuracy,
            "streak_days":  self.store.streak_days(),
            "total_reviews": len(reviews),
        }

    def reviews_per_day(self, n_days: int = 14) -> list[dict]:
        reviews = self.store.all_reviews()
        result  = []
        for i in range(n_days - 1, -1, -1):
            d    = (date.today() - timedelta(days=i)).isoformat()
            cnt  = sum(1 for r in reviews if r.get("date") == d)
            result.append({"date": d, "count": cnt})
        return result

    def weak_topics(self, all_cards: list[dict], n: int = 6) -> list[dict]:
        return self._topic_mastery(all_cards, reverse=False)[:n]

    def strong_topics(self, all_cards: list[dict], n: int = 6) -> list[dict]:
        return self._topic_mastery(all_cards, reverse=True)[:n]

    def _topic_mastery(self, all_cards: list[dict], reverse: bool) -> list[dict]:
        from collections import defaultdict
        states   = self.store.all_states()
        buckets  = defaultdict(list)
        for c in all_cards:
            st = states.get(c["id"], __import__("core.srs_engine", fromlist=["CardState"]).CardState(card_id=c["id"]))
            buckets[c.get("topic", "General")].append(self.engine.mastery_score(st))
        out = [{"topic": t, "mastery": sum(v)/len(v)} for t, v in buckets.items()]
        return sorted(out, key=lambda x: x["mastery"], reverse=reverse)

    def topic_mastery_heatmap(self, all_cards: list[dict]) -> list[dict]:
        from collections import defaultdict
        states  = self.store.all_states()
        buckets = defaultdict(list)
        for c in all_cards:
            st = states.get(c["id"], __import__("core.srs_engine", fromlist=["CardState"]).CardState(card_id=c["id"]))
            key = (c.get("domain", ""), c.get("topic", ""))
            buckets[key].append(self.engine.mastery_score(st))
        return [
            {"domain": d, "topic": t, "mastery": sum(v)/len(v)}
            for (d, t), v in buckets.items()
        ]

    def projected_forgetting_curves(self, all_cards: list[dict]) -> list[dict]:
        import math
        states  = self.store.all_states()
        results = []
        for c in all_cards[:8]:
            st = states.get(c["id"], __import__("core.srs_engine", fromlist=["CardState"]).CardState(card_id=c["id"]))
            if not st.last_review:
                continue
            curve = [(t, math.exp(-t / max(st.stability, 0.1))) for t in range(0, 31, 2)]
            results.append({"front": c["front"], "curve": curve})
        return results
