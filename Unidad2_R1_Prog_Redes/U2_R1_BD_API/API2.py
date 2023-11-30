###Alan Francisco Emmanuel Aguilar Fuentes
### Programacion de Redes
### Api 2 traductor 
import http.client

# Clave de API 
API_KEY = "0ceb9beaf7msh48113a6f6b7e45ep1b530bjsn77587cdf5efc"

def translate_text(source_language, target_language, text):
    """
    Esta API traduce un texto desde un idioma de origen a un idioma de destino utilizando un servicio de traducción.

    Args:
        source_language (str): Idioma de origen del texto.
        target_language (str): Idioma de destino al cual se desea traducir el texto.
        text (str): Texto que se va a traducir.

    Returns:
        str: El resultado de la traducción.

    Raises:
        Exception: Si hay algún problema con la solicitud de traducción.
    """
    conn = http.client.HTTPSConnection("text-translator2.p.rapidapi.com")
    payload = f"source_language={source_language}&target_language={target_language}&text={text}"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
    }

    conn.request("POST", "/translate", payload, headers)
    res = conn.getresponse()

    if res.status != 200:
        raise Exception(f"Error en la solicitud de traducción. Código de estado: {res.status}")

    return res.read().decode("utf-8")

def main():
    """
    Función principal que solicita al usuario información necesaria para la traducción
    y muestra el resultado de la traducción. Permite al usuario salir del programa.

    Returns:
        None
    """
    while True:
        source_language = input("Idioma de origen: ")
        target_language = input("Idioma de destino: ")
        text = input("Texto a traducir: ")

        if not all((source_language, target_language, text)):
            print("Por favor, ingrese valores válidos.")
            continue

        try:
            result = translate_text(source_language, target_language, text)
            print("Resultado de la traducción:", result)
        except Exception as e:
            print(f"Error: {e}")

        if input("¿Desea salir? (s/n): ").lower() == 's':
            break

if __name__ == "__main__":
    main()
