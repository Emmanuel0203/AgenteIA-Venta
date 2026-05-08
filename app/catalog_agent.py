import json
from pathlib import Path
from typing import List

from app.models import Product


class CatalogAgent:
    def __init__(self, data_path: str | None = None) -> None:
        default_path = Path(__file__).parent / "data" / "products.json"
        self._data_path = Path(data_path) if data_path else default_path
        self._products = self._load_products()

    def _load_products(self) -> List[Product]:
        raw = json.loads(self._data_path.read_text(encoding="utf-8"))
        return [Product(**item) for item in raw]

    def list_products(self) -> List[Product]:
        return self._products

    def search_products(self, query: str) -> List[Product]:
        terms = [t.lower() for t in query.split() if t.strip()]
        if not terms:
            return []

        matches: List[Product] = []
        for product in self._products:
            haystack = " ".join(
                [
                    product.name,
                    product.category,
                    " ".join(product.tags),
                ]
            ).lower()
            if any(term in haystack for term in terms):
                matches.append(product)
        return matches

    def get_product_by_name(self, name: str) -> Product | None:
        name_lower = name.lower()
        for product in self._products:
            if product.name.lower() == name_lower:
                return product
        return None

    def get_product_by_id(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.id == product_id:
                return product
        return None

