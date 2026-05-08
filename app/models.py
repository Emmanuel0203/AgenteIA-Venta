from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    id: str
    name: str
    category: str
    price: float
    stock: int
    popularity: int
    tags: List[str] = field(default_factory=list)
    related_ids: List[str] = field(default_factory=list)
    premium_id: str | None = None

