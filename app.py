import tkinter as tk
from lib.models.user import User
from lib.views.add_driver_form import DriverForm



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user = User("postgres", "password")
        self.btn = tk.Button(self, text="Открыть новое окно",
                             command=self.open_driver_form)
        self.btn.pack(padx=50, pady=20)

    def open_driver_form(self):
        form = DriverForm(self)
        form.show()


if __name__ == "__main__":
    app = App()
    app.mainloop()
