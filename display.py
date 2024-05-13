import customtkinter as customtki

# Logika odpowiedzialna za tworzenie okna aplikacji

customtki.set_appearance_mode("dark")
customtki.set_default_color_theme("dark-blue")

class App(customtki.CTk):

    def __init__(self):
        super().__init__()

        # Konfiguracja okna
        self.title("Konwerter jednostek")
        self.geometry(f"{1100}x{580}")

        # Konfiguracja siatki
        self.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure((1, 2, 3), weight=2)

        # Napis tytułowy
        self.label = customtki.CTkLabel(self, text="Konwerter Jednostek", font=customtki.CTkFont(size=30, weight="bold"))
        self.label.grid(row=0, column=2, columnspan=3, padx=20, pady=(20, 10))

        # Podpisy wejscia i wyjscia
        self.labelin = customtki.CTkLabel(self, text="Wejście", font=customtki.CTkFont(size=20, weight="bold"))
        self.labelin.grid(row=1, column=1, columnspan=2, padx=20, pady=(20, 0))

        self.labelout = customtki.CTkLabel(self, text="Wyjście", font=customtki.CTkFont(size=20, weight="bold"))
        self.labelout.grid(row=1, column=4, columnspan=2, padx=20, pady=(20, 0))

        # Znak "=" na środku
        self.rowna = customtki.CTkLabel(self, text="=", font=customtki.CTkFont(size=50, weight="bold"))
        self.rowna.grid(row=2, column=3, padx=10, pady=0)

        # Pole wejściowe
        self.entry = customtki.CTkEntry(self, height=55, width=220, placeholder_text="Ilość", fg_color="gray29", corner_radius=8, font=customtki.CTkFont(size=20), justify="center")
        self.entry.grid(row=2, column=2, padx=5, pady=0)

        # Pole wyjściowe
        self.output = customtki.CTkLabel(self, height=55, width=220, text="Placeholder", font=customtki.CTkFont(size=20), fg_color="gray29", corner_radius=8)
        self.output.grid(row=2, column=4, padx=5, pady=0)

        # Lista jednostek wejścia
        self.listain = customtki.CTkComboBox(self, width=150,
                                             values=["ocpja1", "opcja2", "opcja3"])
        self.listain.grid(row=2, column=1, padx=0, pady=10)

        # Lista jednostek wyjścia
        self.listain = customtki.CTkComboBox(self, width=150,
                                             values=["ocpja1", "opcja2", "opcja3"])
        self.listain.grid(row=2, column=5, padx=0, pady=10)
        
        # Przycisk do konwersjii
        self.button = customtki.CTkButton(self, height=40, width=180, text="Konwertuj")
        self.button.grid(row=3, column=2, columnspan= 3)


if __name__ == "__main__":
    app = App()
    app.mainloop()