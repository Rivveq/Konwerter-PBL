import json

#Główny plik odpowiedzialny za przeprowadzanie konwersji jednostek

#Otwieranie pliku .json z danymi jednostek
with open('jednostki.json') as plik:
    dane_jednostek = json.load(plik)
