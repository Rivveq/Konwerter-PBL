import json
import display

# Główny plik odpowiedzialny za przeprowadzanie konwersji jednostek

# Otwieranie pliku .json z danymi jednostek
with open('jednostki.json') as plik:
    dane_jednostek = json.load(plik)



# Główny loop wyświetlający okno zaimportowane z oliku dispaly.py
if __name__ == "__main__":
    app = display.App()
    app.mainloop()