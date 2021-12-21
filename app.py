import tkinter as tk
from tkinter import *
from source.models.user import User
from source.views.add_driver_form import DriverForm
from source.views.working_drivers_table import WorkingDrivers


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.eval('tk::PlaceWindow . center')
        self.user = User("postgres", "password")
        self.geometry("700x500")
        self.menubar = tk.Menu(self)
        self.build_menu()

    def open_driver_form(self):
        DriverForm(self)

    def open_working_drivers_table(self):
        WorkingDrivers(self)

    def build_menu(self):
        self.config(menu=self.menubar)
        drivers_menu = Menu(self.menubar, tearoff=0)
        drivers_menu.add_command(label="Работающие", command=self.open_working_drivers_table)
        drivers_menu.add_command(label="Регистрация", command=self.open_driver_form)
        self.menubar.add_cascade(label="Водители", menu=drivers_menu)

        orders_menu = Menu(self.menubar, tearoff=0)
        orders_menu.add_command(label="Добавить")
        orders_menu.add_command(label="Статистика")
        self.menubar.add_cascade(label="Заказы", menu=orders_menu)


if __name__ == "__main__":
    app = App()
    app.mainloop()
