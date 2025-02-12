import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")

if __name__ == "__main__":
    app = App()
    app.mainloop()
