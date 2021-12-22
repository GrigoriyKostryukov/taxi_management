class Districts:
    names = {"Дзержинский": 1,
             "Заволжский": 2,
             "Кировский": 3,
             "Красноперекопский": 4,
             "Ленинский": 5,
             "Фрунзенский": 6}

    @staticmethod
    def name_by_id(index):
        keylist = list(Districts.names.keys())
        return keylist[index - 1]

    @staticmethod
    def id_by_name(name):
        return Districts.names[name]

    @staticmethod
    def all_names():
        return list(Districts.names.keys())
