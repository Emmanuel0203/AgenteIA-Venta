from app.orchestrator import SalesOrchestrator


def main() -> None:
    print("Sexmonions Shop AI Agent")
    print("Escribe 'salir' para terminar.\n")
    bot = SalesOrchestrator()

    while True:
        user_input = input("Tu: ").strip()
        if user_input.lower() in {"salir", "exit", "quit"}:
            print("Bot: Hasta pronto.")
            break
        if not user_input:
            continue
        result = bot.handle(user_input)
        print(f"Bot [{result.intent}]: {result.message}\n")


if __name__ == "__main__":
    main()

