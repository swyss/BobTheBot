class Chatbot:
    def __init__(self, name):
        self.name = name

    def get_response(self, message):
        message = message.lower()
        if "hallo" in message:
            return "Hallo! Wie kann ich dir helfen?"
        elif "wie geht's" in message or "wie geht es dir" in message:
            return f"Mir geht's gut, danke! Und dir, {self.name}?"
        elif "witz" in message:
            return "Warum gehen Geister nie zum Doktor? Weil sie keinen Körper haben!"
        else:
            return "Entschuldigung, ich verstehe die Frage nicht. Kannst du sie anders formulieren?"
