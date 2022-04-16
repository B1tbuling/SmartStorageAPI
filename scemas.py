from datetime import datetime

from pydantic import BaseModel


class SensorData(BaseModel):
    id:int = None
    temperature:float = None
    humidity:float = None
    co:float = None
    time:datetime = None


class SensorOneData(BaseModel):
    temperature:float = None
    time:datetime = None


class SensorTwoData(BaseModel):
    humidity:float = None
    time:datetime = None


class SensorThreeData(BaseModel):
    co:float = None
    time:datetime = None


class AddSensorsData(BaseModel):
    temperature:float = None
    humidity:float = None
    co:float = None


class User(BaseModel):
    id:int = None
    name:str = None
    id_touch:str = None
    position:str = None
    exist:bool = None
    last_action_time:datetime = None

class ActivateUser(BaseModel):
    id_touch:str = None