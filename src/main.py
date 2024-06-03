import tkinter as tk
import scraper

class GUI:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Poly's HTML Scraper")
        self.root.geometry('300x300')

        self.top_text = tk.Label(self.root, text="Paste your link below", font=('Arial', 18))
        self.top_text.pack(padx=5, pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Download", font=('Arial', 12), command=self.download_webpage)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()
    
    def download_webpage(self):
        with open('src/web_link.txt', 'w') as file:
            file.write(self.entry.get())
        scraper.WebDown()

GUI()