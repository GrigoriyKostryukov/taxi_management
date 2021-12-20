import tkinter as tk
from tkinter import *
from lib.models.user import User
from lib.views.add_driver_form import DriverForm


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.eval('tk::PlaceWindow . center')
        self.user = User("postgres", "password")
        self.geometry("700x500")
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        drivers_menu = Menu(menubar, tearoff=0)
        drivers_menu.add_command(label="Добавить", command=self.open_driver_form)
        menubar.add_cascade(label="Водители", menu=drivers_menu)

    def open_driver_form(self):
        form = DriverForm(self)
        form.show()


if __name__ == "__main__":
    app = App()
    app.mainloop()

