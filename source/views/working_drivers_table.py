import tkinter as tk
from tksheet import *
from tkinter import *
from tkinter import ttk, messagebox

from source.models.car import Car
from source.models.driver import Driver
from source.db_client import DatabaseClient


class WorkingDrivers(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Водители на маршрутах')
        self.geometry('800x550')
        self.config(bg='#0B5A81')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(self.frame,
                           data=[[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(500)])
        self.sheet.enable_bindings()
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")
        self.build_table()


    def view(self):
        pass

    def build_table(self):
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="ID")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Номер автомобиля")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="LNAME")
        self.tree.pack()
