import http.client

API_KEY = "0ceb9beaf7msh48113a6f6b7e45ep1b530bjsn77587cdf5efc"

def translate_text(source_language, target_language, text):
    conn = http.client.HTTPSConnection("text-translator2.p.rapidapi.com")
    payload = f"source_language={source_language}&target_language={target_language}&text={text}"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
    }

    conn.request("POST", "/translate", payload, headers)
    res = conn.getresponse()
    return res.read().decode("utf-8")

def main():
    while True:
        source_language = input("Idioma de origen: ")
        target_language = input("Idioma de destino: ")
        text = input("Texto a traducir: ")

        if not all((source_language, target_language, text)):
            print("Por favor, ingrese valores válidos.")
            continue

        result = translate_text(source_language, target_language, text)
        print("Resultado de la traducción:", result)

        if input("¿Desea salir? (s/n): ").lower() == 's':
            break

if __name__ == "__main__":
    main()

