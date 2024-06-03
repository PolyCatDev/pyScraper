import customtkinter as ctk
import scraper

class GUI:

    def __init__(self):
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.root = ctk.CTk()

        self.root.title("PyScraper")
        self.root.geometry('300x300')

        self.top_text = ctk.CTkLabel(self.root, text="Paste your link below", font=('Arial', 18))
        self.top_text.pack(padx=5, pady=10)

        self.entry = ctk.CTkEntry(self.root)
        self.entry.pack(padx=10, pady=10)

        self.button = ctk.CTkButton(self.root, text="Download", font=('Arial', 12), command=self.download_webpage)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def download_webpage(self):
        with open('src/web_link.txt', 'w') as file:
            file.write(self.entry.get())
        scraper.WebDown()

GUI()