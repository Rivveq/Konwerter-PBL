import requests
import json
import logika

# Open file
with open('jednostki.json', 'r', encoding='utf-8') as file:
    dane_jednostek = json.load(file)

def convert_currency(input, output, quantity: float):
    """This function converts the input currency to the output currency with a specified quantity of said currency.
    
    Args:
        - input: input currency code.
        - output: output currency code.
        - quantity (float): quantity to be converted.
    
    Returns:
        float: quantity of currency after the conversion.
    """

    conv_from = logika.get_item('waluty', input)
    conv_to = logika.get_item('waluty', output)

    response = requests.get(f"https://api.frankfurter.app/latest?ammount={quantity}&from={conv_from}&to={conv_to}")

    return response.json()['rates'][conv_to]*quantity