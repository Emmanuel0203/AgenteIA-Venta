from fastapi import FastAPI
from pydantic import BaseModel

from app.orchestrator import SalesOrchestrator

app = FastAPI(title="Sexmonions Shop AI Agent")
orchestrator = SalesOrchestrator()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    intent: str
    response: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    result = orchestrator.handle(request.message)
    return ChatResponse(intent=result.intent, response=result.message)

