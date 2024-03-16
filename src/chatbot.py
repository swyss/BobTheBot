from responder import Responder

class Chatbot:
    def __init__(self):
        self.responder = Responder()

    def start_chat(self):
        print("Chatbot: Hallo! Ich bin Ihr virtueller Assistent. Wie kann ich Ihnen helfen?")
        while True:
            user_input = input("Sie: ")
            response = self.responder.get_response(user_input)
            print(f"Chatbot: {response}")
            if "tschüss" in user_input.lower() or "auf wiedersehen" in user_input.lower():
                break
