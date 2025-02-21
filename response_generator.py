import cohere
from config import COHERE_API_KEY
from data_loader import leer_datos_externos
from sentiment_analysis import detectar_emocion, ajustar_tono

co = cohere.Client(COHERE_API_KEY)

def generar_respuesta(user_message):
    """Generates an AI response based on external data and sentiment."""
    
    datos_externos = leer_datos_externos()
    emocion = detectar_emocion(user_message)

    prompt = f"""
    You are an AI assistant for X.
    
    Market Data:
    {datos_externos}

    User message: {user_message}
    Detected emotion: {emocion}

    AI Response:
    """

    response = co.generate(
        model="command-xlarge-nightly",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )

    return ajustar_tono(response.generations[0].text.strip(), emocion)
