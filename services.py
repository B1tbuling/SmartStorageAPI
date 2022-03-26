from math import ceil
from statistics import mean

from db import get_sensors_data_by_time_period


def parting(data, amount):
    part_len = ceil(len(data)/amount)
    return [data[part_len*k:part_len*(k+1)] for k in range(amount)]

def form_data(period: str, amount: int):
    data = get_sensors_data_by_time_period(period)
    splinted_data = parting(data, amount)

    avg_co = []
    avg_hum = []
    avg_temp = []
    avg_time = []
    for sensors_data_segment in splinted_data:
        co_values = []
        hum_values = []
        temp_values = []
        time_values_append = []
        for sensor_data in sensors_data_segment:
            if not sensor_data:
                continue
            co_values.append(sensor_data.Co)
            hum_values.append(sensor_data.Humidity)
            temp_values.append(sensor_data.Temperature)
            time_values_append.append(sensor_data.Time)
        avg_co.append(round(mean(co_values)))
        avg_hum.append(round(mean(hum_values), 2))
        avg_temp.append(round(mean(temp_values), 1))
        avg_time.append(time_values_append[0])
    avg_co.reverse()
    avg_hum.reverse()
    avg_temp.reverse()
    avg_time.reverse()
    return {
        "co": avg_co,
        "hum": avg_hum,
        "temp": avg_temp,
        "time": avg_time
    }

