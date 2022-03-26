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
    ID_Touch:str = None
    Position:str = None
    Exist:bool = None
    Last_Action_Time:datetime = None

class ActivateUser(BaseModel):
    ID_Touch:str = None