import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x600")
        # Widgets
        self.accounts = ctk.CTkButton(self, text="Contas")
        self.accounts.grid(column=0, row=0, padx=20, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
