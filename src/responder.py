class Responder:
    def get_response(self, user_input):
        user_input = user_input.lower()
        if "hallo" in user_input or "hi" in user_input:
            return "Hallo! Wie kann ich Ihnen helfen?"
        elif "wie geht es dir" in user_input:
            return "Mir geht es gut, danke! Und Ihnen?"
        elif "tschüss" in user_input or "auf wiedersehen" in user_input:
            return "Auf Wiedersehen! Schön, dass wir uns unterhalten haben."
        else:
            return "Entschuldigung, ich verstehe die Frage nicht. Können Sie sie bitte umformulieren?"
