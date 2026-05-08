from app.catalog_agent import CatalogAgent
from app.models import Product


class SalesAgent:
    def __init__(self, catalog: CatalogAgent) -> None:
        self.catalog = catalog

    def suggest_upsell(self, product: Product) -> Product | None:
        if not product.premium_id:
            return None
        return self.catalog.get_product_by_id(product.premium_id)

    def suggest_cross_sell(self, product: Product) -> list[Product]:
        suggestions: list[Product] = []
        for related_id in product.related_ids:
            related = self.catalog.get_product_by_id(related_id)
            if related:
                suggestions.append(related)
        return suggestions

    def build_sales_pitch(self, product: Product) -> str:
        upsell = self.suggest_upsell(product)
        cross = self.suggest_cross_sell(product)

        lines = [f"Buena eleccion: {product.name} (${product.price:.2f})."]
        if upsell:
            lines.append(
                f"Si buscas una experiencia premium, te recomiendo {upsell.name} (${upsell.price:.2f})."
            )
        if cross:
            top_cross = ", ".join(p.name for p in cross[:2])
            lines.append(
                f"Tambien podria combinar muy bien con: {top_cross}."
            )
        lines.append("Quieres ver algo mas para completar tu compra?")
        return " ".join(lines)

