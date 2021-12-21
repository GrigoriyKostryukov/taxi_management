import psycopg2
from source.models.driver import Driver


class DatabaseClient:

    @staticmethod
    def add_driver(operator, driver):
        connection = DatabaseClient.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO drivers (surname, name, patronymic, car_number)
                    VALUES (%s, %s, %s, %s)
                    ''', (driver.surname, driver.name, driver.patronymic, driver.car.number))
        connection.commit()
        connection.close()

    @staticmethod
    def add_car(operator, car):
        connection = DatabaseClient.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO cars (car_number, brand, model, color, car_class)
                            VALUES (%s, %s, %s, %s, %s)
                            ''', (car.number, car.brand, car.model, car.color, car.cost_class))
        connection.commit()
        connection.close()

    @staticmethod
    def connect_to_db():
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="taxi",
            user="postgres",
            password="481580asx",
            port="5432"
        )
        return conn
