import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

from source.models.car import Car
from source.models.driver import Driver
from source.db_client import DatabaseClient


class DriverForm(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Регистрация водителя')
        self.geometry('700x550')
        self.config(bg='#0B5A81')

        self.build()

    def build(self):
        # widgets
        font = ('Calibri', 14)

        frame = Frame(self, bd=1, relief=tk.SOLID, padx=5, pady=5)

        Label(frame, text="Информация о водителе", font=font
              ).grid(row=0, column=0, columnspan=2, sticky='nswe', pady=5)
        Label(frame, text="Фамилия", font=font
              ).grid(row=1, column=0, sticky=W, pady=5)
        Label(frame, text="Имя", font=font
              ).grid(row=2, column=0, sticky=W, pady=5)
        Label(frame, text="Отчество", font=font
              ).grid(row=3, column=0, sticky=W, pady=5)
        Label(frame, text='Информация об автомобиле', font=font
              ).grid(row=4, column=0, sticky=N, pady=5, columnspan=2)
        Label(frame, text='Регистрационный номер', font=font
              ).grid(row=5, column=0, sticky=W, pady=5)
        Label(frame, text="Марка", font=font
              ).grid(row=6, column=0, sticky=W, pady=5)
        Label(frame, text="Модель", font=font
              ).grid(row=7, column=0, sticky=W, pady=5)
        Label(frame, text="Цвет", font=font
              ).grid(row=8, column=0, sticky=W, pady=5)
        Label(frame, text="Класс", font=font
              ).grid(row=9, column=0, sticky=W, pady=5)
        surname = Entry(frame, font=font)
        name = Entry(frame, font=font)
        patronymic = Entry(frame, font=font)

        car_number = Entry(frame, font=font)
        car_brand = Entry(frame, font=font)
        car_model = Entry(frame, font=font)
        car_color = Entry(frame, font=font)
        car_class = ttk.Combobox(frame,
                                 values=[1, 2, 3, 4],
                                 state='readonly', font=font, width=18)

        # widgets placement
        surname.grid(row=1, column=1, pady=10, padx=10)
        name.grid(row=2, column=1, pady=10, padx=10)
        patronymic.grid(row=3, column=1, pady=10, padx=10)
        car_number.grid(row=5, column=1, pady=10, padx=10)
        car_brand.grid(row=6, column=1, pady=10, padx=10)
        car_model.grid(row=7, column=1, pady=10, padx=10)
        car_color.grid(row=8, column=1, pady=10, padx=10)
        car_class.grid(row=9, column=1, pady=10, padx=10)

        button_frame = Frame(frame)

        add_button = Button(
            button_frame,
            text='Добавить',
            command=lambda: self.add_driver(surname.get(),
                                            name.get().strip(),
                                            patronymic.get().strip(),
                                            car_number.get().strip(),
                                            car_brand.get().strip(),
                                            car_model.get().strip(),
                                            car_color.get().strip(),
                                            car_class.get().strip()
                                            ),
            font=font
        )
        cancel_button = Button(button_frame, text='Отмена', font=font, command=self.destroy)
        add_button.grid(row=0, column=0, pady=10, padx=10)
        cancel_button.grid(row=0, column=1, pady=10, padx=10)
        button_frame.grid(row=10, column=0, rowspan=2, columnspan=2, pady=5)
        frame.pack(expand=True, side=TOP)
        self.mainloop()

    def add_driver(self, surname, name, patronymic, car_number, car_brand, car_model, car_color, car_class):
        try:
            car = Car(car_number, car_brand, car_model, car_color, car_class)
            driver = Driver("", surname, name, patronymic, car)
            DatabaseClient.add_car("operator", car)
            DatabaseClient.add_driver("operator", driver)
        except ValueError as e:
            messagebox.showerror("Error", e)
