from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class SensorData(BaseModel):
    Temperature:float = None
    Humidity:float = None 
    Co:float = None
    Time:datetime = None
    ID:int = None


class SensorOneData(BaseModel):
    Temperature:float = None
    Time:datetime = None


class SensorTwoData(BaseModel):
    Humidity:float = None
    Time:datetime = None 


class SensorThreeData(BaseModel):
    Co:float = None
    Time:datetime = None 


class AddSensorsData(BaseModel):
    Temperature:float = None
    Humidity:float = None 
    Co:float = None


class User(BaseModel):
    id:int = None
    Name:str = None
    id_touch:str = None
    position:str = None
    exist:bool = None
    last_action_time:datetime = None

class ActivateUser(BaseModel):
    id_touch:str = None