import requests
import json
import logika

# Otwieranie pliku .json z danymi jednostek
with open('jednostki.json', 'r', encoding='utf-8') as file:
    dane_jednostek = json.load(file)

def convert_currency(input, output, quantity: float):
    conv_from = logika.get_item('waluty', input)
    conv_to = logika.get_item('waluty', output)

    response = requests.get(f"https://api.frankfurter.app/latest?ammount={quantity}&from={conv_from}&to={conv_to}")

    return response.json()['rates'][conv_to]*quantity