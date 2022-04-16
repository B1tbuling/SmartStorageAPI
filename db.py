import uuid

import psycopg2
from psycopg2.extras import RealDictCursor

from scemas import SensorData, SensorOneData, SensorTwoData, SensorThreeData, User


class Postgres:
    HOST = '127.0.0.1'
    PORT = 5432
    USER = 'postgres'
    PASS = '51555'
    NAME = 'smartdb'
    
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
        cur.execute('SELECT * FROM sensorsdata ORDER BY time desc limit 3')
        return [SensorData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_temp_data(limit=1):
    with Postgres() as cur:
        cur.execute(f'SELECT temperature,time FROM sensorsdata ORDER BY time desc limit {limit}')
        return [SensorOneData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_hum_data(limit=1):
    with Postgres() as cur:
        cur.execute(f'SELECT humidity,time FROM sensorsdata ORDER BY time desc limit {limit}')
        return [SensorTwoData(**elemnt) for elemnt in cur.fetchall()]


def get_sensor_co_data(limit=1):
    with Postgres() as cur:
        cur.execute(f'SELECT co,time FROM sensorsdata ORDER BY time desc limit {limit}')
        return [SensorThreeData(**elemnt) for elemnt in cur.fetchall()]


def get_sensors_data_by_time_period(period):
    with Postgres() as cur:
        cur.execute(f'select * from sensorsdata where time >= now() - interval \'{period}\'')
        return [SensorData(**elemnt) for elemnt in cur.fetchall()]


def set_sensors(temp, hum, co):
    with Postgres() as cur:
        cur.execute(f'INSERT INTO sensorsdata (temperature,humidity,co,time) VALUES ({temp},{hum},{co}, now())')


def get_users_data():
    with Postgres() as cur:
        cur.execute(f'SELECT * FROM users order by last_action_time desc')
        return [User(**elemnt) for elemnt in cur.fetchall()]


def activate_user(id_touch):
    with Postgres() as cur:
        cur.execute(f"UPDATE users SET exist = Not exist, last_action_time = now() where id_touch = '{id_touch}'")
        cur.execute(f"""
            INSERT 
            INTO users_action 
            (id_touch, exist, action_time)
            VALUES ('{id_touch}', 
            (SELECT exist FROM users where id_touch = '{id_touch}'), 
            now())
        """)


def get_data_sensor(period):
    filename = uuid.uuid4()
    with Postgres() as cur:
        cur.execute(f"""
        COPY (
            select *
            from sensorsdata 
            where time >= now() - interval '{period} hours'
            order by time desc
        )
        To '/tmp/smart_storage/{filename}.csv'
        With CSV
        DELIMITER ',' 
        HEADER;
        """)
        print(period)
        return '/tmp/smart_storage/' + filename + '.csv'


def get_data_user(period):
    filename = uuid.uuid4()
    with Postgres() as cur:
        cur.execute(f"""
        COPY (
            select ua.id, name, ua.exist, action_time
            from users
            join users_action ua
                on users.id_touch = ua.id_touch
            where action_time >= now() - interval '{period}'
        )
        To '/tmp/smart_storage/{filename}.csv'
        With CSV
        DELIMITER ',' 
        HEADER;
        """)
        print(period)
        return '/tmp/smart_storage/' + filename + '.csv'