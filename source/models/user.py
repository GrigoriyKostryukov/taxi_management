import psycopg2


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host="127.0.0.1",
            database="test_db",
            user=self.login,
            password=self.password,
            port="5432"
        )

