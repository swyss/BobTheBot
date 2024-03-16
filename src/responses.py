def basic_responses(message):
    message = message.lower()
    if "hallo" in message:
        return "Hallo! Wie kann ich dir helfen?"
    elif "wie geht's" in message or "wie geht es dir" in message:
        return "Mir geht's gut, danke! Wie geht es dir?"
    elif "witz" in message:
        return "Warum gehen Geister nie zum Doktor? Weil sie keinen Körper haben!"
    else:
        return "Entschuldigung, ich verstehe die Frage nicht. Kannst du sie anders formulieren?"
