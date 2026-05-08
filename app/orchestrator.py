from dataclasses import dataclass

from app.catalog_agent import CatalogAgent
from app.recommender_agent import RecommenderAgent
from app.sales_agent import SalesAgent


@dataclass
class AgentResponse:
    intent: str
    message: str


class SalesOrchestrator:
    def __init__(self) -> None:
        self.catalog = CatalogAgent()
        self.recommender = RecommenderAgent(self.catalog)
        self.sales = SalesAgent(self.catalog)

    def detect_intent(self, user_message: str) -> str:
        text = user_message.lower()
        if any(k in text for k in ["recomiend", "sugier", "que me sugieres"]):
            return "recommend"
        if any(k in text for k in ["precio", "cuanto vale", "cuanto cuesta"]):
            return "price_query"
        if any(k in text for k in ["comprar", "llevar", "me gusta", "agregar"]):
            return "buy_intent"
        if any(k in text for k in ["buscar", "tienes", "mostrar", "producto"]):
            return "search"
        return "search"

    def handle(self, user_message: str) -> AgentResponse:
        intent = self.detect_intent(user_message)

        if intent == "recommend":
            recs = self.recommender.recommend(user_message)
            names = ", ".join(f"{p.name} (${p.price:.2f})" for p in recs)
            return AgentResponse(
                intent=intent,
                message=f"Te recomiendo: {names}.",
            )

        if intent == "price_query":
            cleaned = self._clean_product_query(user_message)
            if not cleaned:
                return AgentResponse(
                    intent=intent,
                    message="Claro. Dime el nombre o categoria del producto para darte el precio.",
                )
            matches = self.catalog.search_products(cleaned)
            if not matches:
                return AgentResponse(
                    intent=intent,
                    message="No encontre ese producto. Prueba con otro nombre o categoria.",
                )
            product = matches[0]
            return AgentResponse(
                intent=intent,
                message=f"El precio de {product.name} es ${product.price:.2f} y tenemos {product.stock} unidades.",
            )

        if intent == "buy_intent":
            matches = self.catalog.search_products(user_message)
            if not matches:
                return AgentResponse(
                    intent=intent,
                    message="Perfecto, te ayudo a comprar. Dime el producto exacto que te interesa.",
                )
            pitch = self.sales.build_sales_pitch(matches[0])
            return AgentResponse(intent=intent, message=pitch)

        matches = self.catalog.search_products(user_message)
        if not matches:
            return AgentResponse(
                intent=intent,
                message="No encontre resultados en el catalogo. Puedes intentar por categoria: lenceria, bienestar o accesorios.",
            )
        lines = [
            f"{p.name} - ${p.price:.2f} ({p.category}, stock: {p.stock})"
            for p in matches[:5]
        ]
        return AgentResponse(
            intent=intent,
            message="Encontre estos productos:\n- " + "\n- ".join(lines),
        )

    def _clean_product_query(self, text: str) -> str:
        stopwords = {
            "cual",
            "cuanto",
            "vale",
            "cuesta",
            "precio",
            "del",
            "de",
            "el",
            "la",
            "los",
            "las",
            "es",
            "quiero",
            "saber",
        }
        tokens = [t for t in text.lower().replace("?", "").split() if t not in stopwords]
        return " ".join(tokens).strip()

