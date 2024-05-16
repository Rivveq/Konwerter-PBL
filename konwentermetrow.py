def meters_to_kilometers(meters):
    return meters / 1000

def meters_to_miles(meters):
    return meters / 1609.344

def meters_to_feet(meters):
    return meters * 3.28084

def meters_to_inches(meters):
    return meters * 100

def main():
    print("Konwenter metrów na jednostki")
    print("1: Metry na kilometry")
    print("2: Metry na mile")
    print("3: Metry na stopy")
    print("4: Metry na centymetry")

    choice = int(input("Wybierz numer od 1-4: "))

    if choice in [1, 2, 3, 4]:
        meters = float(input("Ile metrów "))
        if choice == 1:
            print(f"{meters} m to {meters_to_kilometers(meters)} km")
        elif choice == 2:
            print(f"{meters} m to {meters_to_miles(meters)} mil")
        elif choice == 3:
            print(f"{meters} m to {meters_to_feet(meters)} stóp")
        elif choice == 4:
            print(f"{meters} m to {meters_to_inches(meters)} cm")
    else:
        print("Zły wybór")

if __name__ == "__main__":
    main()
