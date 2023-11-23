#Api
#Alan Francisco Emmanuel Aguilar Fuentes
# Profesor: Gabriel Barrón R.

import requests

while True:
    symbol = input("Ingrese el símbolo (por ejemplo, 'MSFT'): ")
    
    options = {
        'method': 'GET',
        'url': 'https://alpha-vantage.p.rapidapi.com/query',
        'params': {
            'symbol': symbol,
            'function': 'TIME_SERIES_INTRADAY',
            'interval': '5min',
            'output_size': 'compact',
            'datatype': 'json'
        },
        'headers': {
            'X-RapidAPI-Key': '096cb21923mshdca5fb2e3286a06p12267ajsn27888e4f8ddc',
            'X-RapidAPI-Host': 'alpha-vantage.p.rapidapi.com'
        }
    }

    try:
        response = requests.request(**options)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print(data)
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")

    seguir = input("¿Quiere seguir (S) o salir (Enter)? ").lower()
    if seguir != 's':
        break
