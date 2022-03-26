from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from scemas import AddSensorsData, ActivateUser
from db import get_last_three_value, get_sensor_temp_data, get_sensor_hum_data, get_sensor_co_data, set_sensors, \
    get_users_data, activate_user
from services import form_data


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_data():
    return get_last_three_value()


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
    set_sensors(data.Temperature, data.Humidity, data.Co)


@app.get("/users")
def getUsers():
    return get_users_data()


@app.post("/activateUser")
def activateUser(ID_Touch: ActivateUser):
    activate_user(ID_Touch.ID_Touch)