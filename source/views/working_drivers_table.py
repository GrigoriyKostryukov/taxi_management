import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from source.db_client import DatabaseClient
from source.models.districts import Districts


class WorkingDrivers(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.selected_driver_status = DriverStatus()
        title = Label(self, text="Положение водителей", font=("Calibri", 20))
        title.pack(side=TOP)
        self.table_frame = Frame(self)
        self.edit_frame = Frame(self)
        self.tree = ttk.Treeview(self.table_frame)
        self.district_combobox = ttk.Combobox()
        self.build_editing_form()
        self.build_table()

    def build_table(self):

        self.table_frame.pack(side=LEFT, expand=True, fill='y', padx=5, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.select_driver)
        self.tree['columns'] = ("ID", "sur", "name", "car", "district", "status")
        self.tree['show'] = 'headings'
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column("ID", width=50, anchor=E)
        self.tree.column("sur", width=150, anchor=CENTER)
        self.tree.column("name", width=150, anchor=CENTER)
        self.tree.column("car", width=120, anchor=CENTER)
        self.tree.column("status", width=100, anchor=CENTER)
        self.tree.column("car", width=100, anchor=CENTER)
        self.tree.column("district", width=150, anchor=CENTER)
        self.tree.heading('#0', text='')
        self.tree.heading("ID", text="ID")
        self.tree.heading("sur", text="Фамилия")
        self.tree.heading("name", text="Имя")
        self.tree.heading("car", text="Автомобиль")
        self.tree.heading("status", text="Статус")
        self.tree.heading("district", text="Район")

        self.tree.pack(expand=True, fill=BOTH)

    def process_status(self, driver_info):
        if driver_info[5]:
            driver_info[5] = 'Занят'
        else:
            driver_info[5] = 'Свободен'
        return driver_info

    def build_editing_form(self):
        self.edit_frame.pack(side=RIGHT, expand=True, fill='y', padx=10, pady=10)
        Calibri12 = ("Calibri", 12)
        Calibri14 = ("Calibri", 14)
        status_frame = Frame(self.edit_frame)
        status_lb = Label(status_frame, text="Статус", font=Calibri14)
        district_lb = Label(status_frame, text="Район", font=Calibri14)
        radiobuttons_frame = Frame(status_frame)
        free = Radiobutton(radiobuttons_frame, text='Свободен',
                           variable=self.selected_driver_status.busy, value=False, font=Calibri12)
        busy = Radiobutton(radiobuttons_frame, text='Занят',
                           variable=self.selected_driver_status.busy, value=True, font=Calibri12)
        free.grid(row=0, column=0)
        busy.grid(row=0, column=1)
        buttons_frame = Frame(status_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=5)
        edit = Button(buttons_frame, text="Изменить", font=Calibri12, command=self.change_driver_status)
        stop = Button(buttons_frame, text="Завершить работу", font=Calibri12, command=self.stop_driver_work)

        self.district_combobox = ttk.Combobox(status_frame,
                                              values=Districts.all_names(),
                                              state='readonly', width=17, font=Calibri12, )
        self.district_combobox.bind('<<ComboboxSelected>>',
                                    lambda _event: self.set_district_value(self.district_combobox.get()))
        status_lb.grid(row=0, column=0, pady=5, padx=10)
        radiobuttons_frame.grid(row=0, column=1, columnspan=2, pady=5)
        district_lb.grid(row=2, column=0, pady=5, padx=10)
        self.district_combobox.grid(row=2, column=1, columnspan=2, pady=5)
        edit.pack(side=RIGHT)
        stop.pack(side=LEFT, padx=15)

        status_frame.pack(expand=TRUE)
        self.update_info()

    def select_driver(self, _event):
        item_id = self.tree.focus()
        info = self.tree.item(item_id)['values']
        self.selected_driver_status.update(info[0], info[4], info[5])
        self.district_combobox.set(self.selected_driver_status.driver_district)

    def set_district_value(self, district):
        self.selected_driver_status.driver_district = district

    def change_driver_status(self):
        if not self.selected_driver_status.driver_id:
            messagebox.showerror("Ошибка", "Водитель не выбран")
            return
        DatabaseClient.update_driver_status("", self.selected_driver_status)
        self.selected_driver_status.reset()
        self.update_info()

    def stop_driver_work(self):
        if not self.selected_driver_status.driver_id:
            messagebox.showerror("Ошибка", "Водитель не выбран")
            return
        self.selected_driver_status.reset()
        DatabaseClient.stop_driver_work("", self.selected_driver_status.driver_id)
        self.update_info()

    def update_info(self):
        self.selected_driver_status.reset()
        for item in self.tree.get_children():
            self.tree.delete(item)
        drivers = DatabaseClient.working_drivers("")
        for i in range(len(drivers)):
            self.tree.insert(index=i, values=self.process_status(list(drivers[i])), parent='')
            print(self.process_status(list(drivers[i])))


class DriverStatus:

    def __init__(self):
        self.driver_id = None
        self.driver_district = None
        self.busy = BooleanVar()
        self.busy.set(False)

    def update(self, id, district, busy):
        self.driver_id = id
        self.busy.set(busy == "Занят")
        self.driver_district = district

    def reset(self):
        self.driver_id = None
        self.driver_district = None