"""A beginner-friendly rule-based terminal chatbot."""
import random

RESPONSES = {
    "greeting": [
        "Hello! How are you today?",
        "Hi! What would you like to talk about?",
        "Hey there! Ready to learn something new?"
    ],
    "help": [
        "I can chat, answer simple prompts, and help you practice Python.",
        "Try saying hello, asking how I am, or typing 'help'."
    ],
    "feeling": [
        "I'm running well, thanks for asking!",
        "All systems are ready. How can I help?"
    ],
    "learning": [
        "A good way to learn Python is to build small projects every day.",
        "Try changing one part of this code and observe what happens."
    ],
    "fallback": [
        "I'm not sure I understand yet. Try asking in a different way.",
        "I don't know that one yet, but you can teach me by adding a rule.",
        "Interesting! My next upgrade should learn how to answer that."
    ],
    "goodbye": [
        "Goodbye! Keep learning.",
        "See you next time. Happy coding!"
    ],
}


def get_response(message: str) -> str:
    """Choose a response based on simple keywords."""
    text = message.lower().strip()

    if any(word in text for word in ("bye", "exit", "quit")):
        return random.choice(RESPONSES["goodbye"])
    if any(word in text for word in ("hello", "hi", "hey", "сәлем")):
        return random.choice(RESPONSES["greeting"])
    if "help" in text or "көмек" in text or "can you do" in text:
        return random.choice(RESPONSES["help"])
    if "how are you" in text or "қалайсың" in text:
        return random.choice(RESPONSES["feeling"])
    if any(word in text for word in ("python", "learn", "үйрен", "study")):
        return random.choice(RESPONSES["learning"])
    return random.choice(RESPONSES["fallback"])


def main() -> None:
    print("Smart Chatbot")
    print("Type 'bye', 'exit', or 'quit' to stop.\n")

    while True:
        try:
            message = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Keep learning.")
            break

        if not message:
            print("Bot: Type something and I'll try to respond.")
            continue

        response = get_response(message)
        print(f"Bot: {response}")

        if any(word in message.lower().strip() for word in ("bye", "exit", "quit")):
            break


if __name__ == "__main__":
    main()
