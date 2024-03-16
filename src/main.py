from chatbot import Chatbot

def main():
    bot = Chatbot("Benutzer")
    print("Chatbot: Hallo! Ich bin ein freundlicher Chatbot. Wie kann ich dir helfen? Schreib 'tschüss' um das Gespräch zu beenden.")

    while True:
        user_input = input("Du: ")
        if user_input.lower() == "tschüss":
            print("Chatbot: Tschüss! Bis zum nächsten Mal!")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
