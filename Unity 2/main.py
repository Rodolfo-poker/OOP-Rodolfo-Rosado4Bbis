import tkinter as tk
from models_lab8.user_model import UserModel
from views_lab8.login_view import LoginView
from controllers_lab8.authentication_controller import Authentication


class System:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.start()