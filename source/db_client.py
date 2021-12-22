import psycopg2

from source.models.districts import Districts
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
    def working_drivers(operator):
        connection = DatabaseClient.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''SELECT working_drivers.driver_id, drivers.surname, drivers.name,  
        drivers.car_number, districts.name, working_drivers.busy
        FROM working_drivers
        JOIN drivers 
	    ON working_drivers.driver_id = drivers."ID"
        JOIN districts 
	    ON working_drivers.location_district = districts."ID";
	    ''')
        results = cursor.fetchall()
        connection.close()
        return results

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
    def update_driver_status(operator, driver_status):
        connection = DatabaseClient.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''UPDATE working_drivers 
        SET (location_district, busy, last_update_time) = (%s, %s, now()::timestamp)
        WHERE driver_id = %s''', (Districts.id_by_name(driver_status.driver_district),
                                  driver_status.busy.get(), driver_status.driver_id))
        connection.commit()
        connection.close()

    @staticmethod
    def stop_driver_work(operator, driver_id):
        connection = DatabaseClient.connect_to_db()
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM working_drivers 
            WHERE driver_id = %s''', (driver_id,))
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
