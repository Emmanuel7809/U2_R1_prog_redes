##Alan Francisco Emmanuel Aguilar Fuentes
## Programacion de Redes
## Gabriel barron 
import http.client
import json

api_key = "0ceb9beaf7msh48113a6f6b7e45ep1b530bjsn77587cdf5efc"

while True:
    try:
        conn = http.client.HTTPSConnection("soundcloud4.p.rapidapi.com")
        headers = {'X-RapidAPI-Key': api_key, 'X-RapidAPI-Host': "soundcloud4.p.rapidapi.com"}
        track_url = input("Ingresa la URL de la canción de SoundCloud ('salir' para salir): ").strip()

        if track_url.lower() == 'salir':
            print("Saliendo del programa.")
            break

        if not track_url:
            print("La URL no puede estar vacía. Inténtalo de nuevo.")
            continue

        api_path = f"/song/info?track_url={track_url}"
        conn.request("GET", api_path, headers=headers)
        res = conn.getresponse()
        api_response = json.loads(res.read().decode("utf-8"))

        artist_name = api_response.get('author', {}).get('name', 'Desconocido')
        track_name = api_response.get('title', 'Desconocido')

        print(f"Artista: {artist_name}")
        print(f"Canción: {track_name}")

    except Exception as e:
        print(f"Error al realizar la solicitud a la API: {e}")

    finally:
        conn.close()



