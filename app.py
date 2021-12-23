import tkinter as tk
from tkinter import *

from source.controllers.order_controller import OrderController
from source.models.order import Order
from source.models.user import User
from source.views.add_working_driver import AddWorkingDriversTable
from source.views.order_form import OrderForm
from source.views.register_driver_form import DriverForm
from source.views.working_drivers_table import WorkingDrivers


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user = User("postgres", "password")
        self.geometry("1000x500")
        self.menubar = tk.Menu(self)
        self.working_drivers_table = WorkingDrivers(self)
        self.working_drivers_table.pack(expand=True, fill=BOTH)
        self.build_menu()

    def open_driver_form(self):
        DriverForm(self)

    def open_working_drivers_table(self):
        WorkingDrivers(self)

    def build_menu(self):
        self.config(menu=self.menubar)
        drivers_menu = Menu(self.menubar, tearoff=0)
        drivers_menu.add_command(label="Новый...", command=self.open_driver_form)
        drivers_menu.add_command(label="Начать работу...", command=self.open_add_working_drivers_table)
        self.menubar.add_cascade(label="Водители", menu=drivers_menu)
        self.menubar.add_command(label="Обновить", command=self.working_drivers_table.update_info)

        orders_menu = Menu(self.menubar, tearoff=0)
        orders_menu.add_command(label="Новый...", command=self.open_order_form)
        orders_menu.add_command(label="Статистика...")
        self.menubar.add_cascade(label="Заказы", menu=orders_menu)

    def open_add_working_drivers_table(self):
        AddWorkingDriversTable(self)

    def open_order_form(self):
        order = Order()
        form = OrderForm(self)
        controller = OrderController(order, form)
        form.set_controller(controller)


if __name__ == "__main__":
    app = App()
    app.mainloop()
