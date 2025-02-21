from textblob import TextBlob

def detectar_emocion(texto):
    """Detects emotion in text using TextBlob."""
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity

    if polaridad > 0.2:
        return "positive"
    elif polaridad < -0.2:
        return "negative"
    return "neutral"

def ajustar_tono(respuesta, emocion):
    """Adjusts response tone based on detected emotion."""
    if emocion == "positive":
        return f"😊 {respuesta}"
    elif emocion == "negative":
        return f"😕 {respuesta}"
    return respuesta
