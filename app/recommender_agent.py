from typing import List

from app.catalog_agent import CatalogAgent
from app.models import Product


class RecommenderAgent:
    def __init__(self, catalog: CatalogAgent) -> None:
        self.catalog = catalog

    def recommend(self, user_message: str, top_k: int = 3) -> List[Product]:
        products = self.catalog.list_products()
        terms = [t.lower() for t in user_message.split() if t.strip()]

        scored: list[tuple[int, Product]] = []
        for p in products:
            score = 0

            if any(term in p.category.lower() for term in terms):
                score += 5
            if any(term in p.name.lower() for term in terms):
                score += 4
            if any(term in " ".join(p.tags).lower() for term in terms):
                score += 3

            score += int(p.popularity / 25)
            scored.append((score, p))

        scored.sort(key=lambda item: item[0], reverse=True)
        ranked = [item[1] for item in scored if item[0] > 0]
        if ranked:
            return ranked[:top_k]

        # Fallback por popularidad cuando no hay contexto.
        return sorted(products, key=lambda p: p.popularity, reverse=True)[:top_k]

