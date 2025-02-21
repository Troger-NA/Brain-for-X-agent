import json

def leer_datos_externos(archivo="datos_externos.json"):
    """Loads external market data from a JSON file."""
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def leer_prompt_base(archivo="prompt_base.txt"):
    """Loads the base prompt from a text file."""
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "You are an AI assistant for X."
