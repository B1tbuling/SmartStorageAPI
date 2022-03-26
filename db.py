import psycopg2
from psycopg2.extras import RealDictCursor

from scemas import SensorData, SensorOneData, SensorTwoData, SensorThreeData, User


class Postgres:
    # Connect to an existing database
    HOST = '127.0.0.1'
    PORT = 5432
    USER = 'postgres'
    PASS = '51555'
    NAME = 'SmartDB'
    
    def __init__(self):
        self.DATABASE_URL = f'postgresql://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}'

    def __enter__(self):
        self.conn = psycopg2.connect(self.DATABASE_URL, cursor_factory=RealDictCursor)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        self.cur.close()


def get_last_three_value():
    with Postgres() as cur:
        cur.execute('SELECT * FROM "SensorsData" ORDER BY "Time" desc limit 3')
        return [SensorData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_temp_data(limit = 1):
    with Postgres() as cur:
        cur.execute(f'SELECT "Temperature","Time" FROM "SensorsData" ORDER BY "Time" desc limit {limit}') 
        return [SensorOneData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_hum_data(limit = 1):
    with Postgres() as cur:
        cur.execute(f'SELECT "Humidity","Time" FROM "SensorsData" ORDER BY "Time" desc limit {limit}')
        return [SensorTwoData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_co_data(limit = 1):
    with Postgres() as cur:
        cur.execute(f'SELECT "Co","Time" FROM "SensorsData" ORDER BY "Time" desc limit {limit}')
        return [SensorThreeData(**elemnt) for elemnt in cur.fetchall()]


def get_sensors_data_by_time_period(period):
    with Postgres() as cur:
        cur.execute(f'select * from "SensorsData" where "Time" >= now() - interval \'{period}\'')
        return [SensorData(**elemnt) for elemnt in cur.fetchall()]


def set_sensors(temp, hum, co):
    with Postgres() as cur:
        cur.execute(f'INSERT INTO "SensorsData" ("Temperature","Humidity","Co","Time") VALUES ({temp},{hum},{co}, now())')


def get_users_data():
    with Postgres() as cur:
        cur.execute(f'SELECT * FROM "Users" order by "Last_Action_Time" desc')
        return [User(**elemnt) for elemnt in cur.fetchall()]


def activate_user(Id_Touch):
    with Postgres() as cur:
        cur.execute(f'UPDATE "Users" set "Exist" = Not "Exist", "Last_Action_Time" = now() where "ID_Touch" = \'{Id_Touch}\'')