from db import Postgres
import random


with Postgres() as cur:
    cur.execute(f'''
        INSERT INTO sensorsdata (temperature, humidity, co)
        values '''+
        ', '.join([f"({random.randint(10, 35)}, {random.randint(1, 80)}, {random.randint(10, 5000)})" for i in range(10000)])
    )


with Postgres() as cur:
    for i in range(1, 10000):
        cur.execute(f'''
            UPDATE sensorsdata SET time = now() - (interval \'5 minutes\'*{i}) WHERE id = {10000-i}
        ''')
