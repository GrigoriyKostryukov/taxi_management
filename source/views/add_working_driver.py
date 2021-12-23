import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from source.db_client import DatabaseClient
from source.models.districts import Districts


class AddWorkingDriversTable(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.table_frame = Frame(self)
        self.bottom_frame = Frame(self)
        self.tree = ttk.Treeview(self.table_frame)
        self.driver_id = None
        self.build_table()
        self.build_bottom_bar()
        self.mainloop()

    def build_table(self):

        self.tree.bind("<<TreeviewSelect>>", self.select_driver)
        self.tree['columns'] = ("ID", "sur", "name", "car")
        self.tree['show'] = 'headings'
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column("ID", width=50, anchor=E)
        self.tree.column("sur", width=150, anchor=CENTER)
        self.tree.column("name", width=150, anchor=CENTER)
        self.tree.column("car", width=120, anchor=CENTER)
        self.tree.heading('#0', text='')
        self.tree.heading("ID", text="ID")
        self.tree.heading("sur", text="Фамилия")
        self.tree.heading("name", text="Имя")
        self.tree.heading("car", text="Автомобиль")
        self.tree.pack(expand=True, fill=BOTH)
        self.table_frame.pack(side=TOP, expand=True, fill='y', padx=10, pady=10)
        self.update_info()

    def select_driver(self, _event):
        item_id = self.tree.focus()
        self.driver_id = self.tree.item(item_id)['values'][0]

    def build_bottom_bar(self):
        self.bottom_frame.pack(side=BOTTOM)
        add_button = Button(self.bottom_frame, text='Добавить', command=self.add_driver)
        add_button.pack(side=LEFT, padx=20, pady=20)

    def add_driver(self):
        if not self.driver_id:
            messagebox.showerror("Ошибка", "Водитель не выбран")
            return
        DatabaseClient.start_driver_work("", self.driver_id)
        self.update_info()

    def update_info(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        drivers = DatabaseClient.get_inactive_drivers()
        for i in range(len(drivers)):
            self.tree.insert(index=i, values=list(drivers[i]), parent='')
