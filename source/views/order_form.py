import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from source.models.car import Car
from source.models.districts import Districts
from source.models.driver import Driver
from source.db_client import DatabaseClient
from source.models.order import Order


class OrderForm(tk.Toplevel):

    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.client_id = StringVar()
        self.phone_number = StringVar()
        self.departure_district = StringVar()
        self.street = StringVar()
        self.house = StringVar()
        self.flat = StringVar()
        self.arrival_district = StringVar()
        self.car = StringVar()

        self.title('Формирование заказа')
        self.geometry('900x600')
        self.config(bg='#0B5A81')
        self.build()

    def set_controller(self, controller):
        self.controller = controller

    def build(self):
        # widgets
        font = ('Calibri', 15)
        font2 = ('Calibri', 12)

        frame = Frame(self, bd=1, relief=tk.SOLID, padx=20, pady=20, )

        Label(frame, text="ID клиента", font=font
              ).grid(row=0, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text="Номер телефона", font=font
              ).grid(row=2, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text="Адрес отправления:", font=font
              ).grid(row=3, column=0, columnspan=2, sticky=W, pady=5, padx=20)
        Label(frame, text="Район", font=font
              ).grid(row=4, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text='Улица', font=font
              ).grid(row=5, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text='Дом', font=font
              ).grid(row=6, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text="Квартира", font=font
              ).grid(row=7, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text="Район прибытия", font=font
              ).grid(row=8, column=0, sticky=W, pady=5, padx=20)
        Label(frame, text="Автомобиль", font=font
              ).grid(row=9, column=0, sticky=W, pady=5, padx=20)

        autofill_button = Button(frame, text="Заполнить поля", command=self.autofill, font=font2)
        select_car_button = Button(frame, text="Выбрать", command=self.autofill, font=font2)

        client_id_entry = Entry(frame, font=font)
        phone_number_entry = Entry(frame, font=font)
        street_entry = Entry(frame, font=font)
        house_entry = Entry(frame, font=font)
        flat_entry = Entry(frame, font=font)
        car_entry = Entry(frame, font=font)

        departure_district_combobox = ttk.Combobox(frame,
                                                   values=Districts.all_names(),
                                                   state='readonly', font=font, width=18)
        arrival_district_combobox = ttk.Combobox(frame,
                                                 values=Districts.all_names(),
                                                 state='readonly', font=font, width=18)

        # widgets placement
        client_id_entry.grid(row=0, column=1, pady=10, padx=10)
        autofill_button.grid(row=0, column=2, pady=10, padx=10, sticky=E)
        phone_number_entry.grid(row=2, column=1, pady=10, padx=10)
        departure_district_combobox.grid(row=4, column=1, pady=10, padx=10, sticky=W)
        street_entry.grid(row=5, column=1, pady=10, padx=10)
        house_entry.grid(row=6, column=1, pady=10, padx=10)
        flat_entry.grid(row=7, column=1, pady=10, padx=10)
        arrival_district_combobox.grid(row=8, column=1, pady=10, padx=10)
        car_entry.grid(row=9, column=1, pady=10, padx=10)
        select_car_button.grid(row=9, column=2, pady=10, padx=10, sticky=W)

        button_frame = Frame(frame)
        accept_button = Button(button_frame, text='Принять', command=self.accept, font=font)
        decline_button = Button(button_frame, text='Отклонить', command=self.decline, font=font)
        accept_button.pack(side=LEFT, padx=10)
        decline_button.pack(side=RIGHT, padx=10)
        button_frame.grid(row=10, column=0, columnspan=3, pady=10, padx=10)
        frame.pack(fill='y', expand=True)
        self.mainloop()

    def autofill(self):
        pass

    def accept(self):
        pass

    def select_car(self):
        self.controller.select_car()

    def decline(self):
        self.destroy()
