import customtkinter as customtki

# Logika odpowiedzialna za tworzenie okna aplikacji

class App(customtki.CTk):

    customtki.set_appearance_mode("dark")
    customtki.set_default_color_theme("dark-blue")

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
        self.label.grid(row=0, column=1, columnspan=3, padx=20, pady=(20, 10))

        # Sidebar
        self.sidebar_frame = customtki.CTkFrame(self, width=180, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=5, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure((1, 2, 3, 4, 5, 6, 7, 8, 9), weight=2)
        self.sidebar_frame.grid_columnconfigure(1, weight=2)

        # Przyciski na sidebarze
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Długość")
        self.sbutton1.grid(row=1, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Masa")
        self.sbutton1.grid(row=2, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Czas")
        self.sbutton1.grid(row=3, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Pole Powierzchni")
        self.sbutton1.grid(row=4, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Objętość")
        self.sbutton1.grid(row=5, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Temperatura")
        self.sbutton1.grid(row=6, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Ciśnienie")
        self.sbutton1.grid(row=7, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Prędkość")
        self.sbutton1.grid(row=8, columnspan=2)
        
        self.sbutton1 = customtki.CTkButton(self.sidebar_frame, height=40, width=120, text="Pojemność Pamięci")
        self.sbutton1.grid(row=9, columnspan=2)


        # Podpisy wejscia i wyjscia
        self.labelin = customtki.CTkLabel(self, text="Wejście", font=customtki.CTkFont(size=20, weight="bold"))
        self.labelin.grid(row=1, column=1, padx=20, pady=(10, 0))

        self.labelout = customtki.CTkLabel(self, text="Wyjście", font=customtki.CTkFont(size=20, weight="bold"))
        self.labelout.grid(row=1, column=3, padx=20, pady=(10, 0))

        # Znak "=" na środku
        self.rowna = customtki.CTkLabel(self, text="=", font=customtki.CTkFont(size=50, weight="bold"))
        self.rowna.grid(row=2, column=2, padx=10, pady=0)

        # Pole wejściowe
        self.entry = customtki.CTkEntry(self, height=55, width=220, placeholder_text="Ilość", fg_color="gray29", corner_radius=8, font=customtki.CTkFont(size=20), justify="center")
        self.entry.grid(row=2, column=1, padx=5, pady=0)

        # Pole wyjściowe
        self.output = customtki.CTkLabel(self, height=55, width=220, text="Placeholder", font=customtki.CTkFont(size=20), fg_color="gray29", corner_radius=8)
        self.output.grid(row=2, column=3, padx=5, pady=0)

        # Lista jednostek wejścia
        self.listain = customtki.CTkComboBox(self, width=150,
                                             values=["ocpja1", "opcja2", "opcja3"])
        self.listain.grid(row=3, column=1, padx=0, pady=10)

        # Lista jednostek wyjścia
        self.listain = customtki.CTkComboBox(self, width=150,
                                             values=["ocpja1", "opcja2", "opcja3"])
        self.listain.grid(row=3, column=3, padx=0, pady=10)
        
        # Przycisk do konwersjii
        self.button = customtki.CTkButton(self, height=40, width=180, text="Konwertuj")
        self.button.grid(row=3, column=1, columnspan=3)