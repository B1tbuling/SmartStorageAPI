from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from scemas import AddSensorsData, ActivateUser
from db import get_sensor_temp_data, get_sensor_hum_data, get_sensor_co_data, set_sensors, \
    get_users_data, activate_user, get_data_sensor, get_data_user
from services import form_data


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/temp")
def get_data(limit=1):
    return get_sensor_temp_data(limit)


@app.get("/hum")
def get_data(limit=1):
    return get_sensor_hum_data(limit)


@app.get("/co")
def get_data(limit=1):
    return get_sensor_co_data(limit)


@app.get("/getSensorsData")
def addData(period: str, amount: int):
    return form_data(period, amount)


@app.post("/addSensors")
def addData(data: AddSensorsData):
    set_sensors(data.temperature, data.humidity, data.co)


@app.get("/users")
def getUsers():
    return get_users_data()


@app.post("/activateUser")
def activateUser(id_touch: ActivateUser):
    activate_user(id_touch.id_touch)


@app.get("/getStatisticSensor")
def getDataSensor(period:str):
    sensor_data = get_data_sensor(period)
    return FileResponse(sensor_data)


@app.get("/getStatisticUser")
def getDataUser(period:str):
    users_data = get_data_user(period)
    return FileResponse(users_data)