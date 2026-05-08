from app.orchestrator import SalesOrchestrator


def test_search_products() -> None:
    bot = SalesOrchestrator()
    response = bot.handle("buscar lenceria encaje negro")
    assert response.intent == "search"
    assert "Encontre estos productos" in response.message


def test_recommendation_intent() -> None:
    bot = SalesOrchestrator()
    response = bot.handle("recomiendame algo de lubricantes")
    assert response.intent == "recommend"
    assert "Te recomiendo" in response.message


def test_sales_pitch_buy_intent() -> None:
    bot = SalesOrchestrator()
    response = bot.handle("quiero comprar lubricante")
    assert response.intent == "buy_intent"
    assert "Quieres ver algo mas" in response.message

