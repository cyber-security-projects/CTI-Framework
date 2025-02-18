import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x600+300+200")
        self.title("Cyber Threat Intelligence Framework")
        self.resizable(False, False)
        # Widgets
        self.accounts = ctk.CTkButton(self, text="Gerenciar contas", command=self.manage_account)
        self.accounts.grid(column=0, row=0, padx=20, pady=20)
    
    def manage_account(self):
        toplevel = ctk.CTkToplevel(self)
        toplevel.title("Gerenciador de contas")
        toplevel.resizable(False, True)
        toplevel.geometry("400x600+700+200")
        

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    app = App()
    app.mainloop()
