import re


class Car:

    def __init__(self, number, brand='N/A', model='N/A', color='N/A', cost_class=4):
        if not self.is_number_valid(number.upper()):
            raise ValueError('''Номер должен соответствовать формату.
                             Пример: А123АА76''')
        self.number = number.upper()
        self.brand = brand
        self.model = model
        self.cost_class = cost_class
        self.color = color

    def is_number_valid(self, value):
        print(value)
        return re.match(r'[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}', value)
