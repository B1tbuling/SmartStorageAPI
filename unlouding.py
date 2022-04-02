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

