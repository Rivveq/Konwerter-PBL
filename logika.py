import json

# Otwieranie pliku .json z danymi jednostek
with open('jednostki.json', 'r', encoding='utf-8') as file:
    dane_jednostek = json.load(file)

# Funkcja do pobierania konkretnego przelicznika
def get(category, item):
    return dane_jednostek[category][item]

# Funkcja do pozyskiwania wspolczynnika konwersji dla konkretnej pary jednostek
def get_convert_factor(category, input, output):
    input_factor = get(category, input)
    output_factor = get(category, output)
    return output_factor/input_factor

# Funkcja do konwertowania pary jednostek
def convert(category, input, output, quantity):
    return float(quantity)*get_convert_factor(category, input, output)

# Funkcja zwracająca listę jednostek z danej kategorii
def fetch_items(category):
    return list(dane_jednostek[category].keys())