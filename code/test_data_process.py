import pandas as pd
import math
from datetime import datetime as dt

def LLs2Dist(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat1 * math.pi / 180.0) * math.cos(lat2 * math.pi / 180.0) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    dist = R * c
    return dist

taxi_file_path = '../datas/new_york_city_taxi_fare_prediction/train.csv'
taxi_data_test_path = '../datas/prepare/test.csv'
taxi_data_test_zip_path = '../data_zipped/test.gz'
taxi_data = pd.read_csv(taxi_file_path,skiprows=range(1,1000000),nrows=200000)
datetime = taxi_data.pickup_datetime
splited = [d.split() for d in datetime]
date = [s[0] for s in splited]
sep_date = [d.split('-') for d in date]
year = [int(s[0]) for s in sep_date]
month = [int(s[1]) for s in sep_date]
day = [int(s[2]) for s in sep_date]
hour = [int(s[1].split(':')[0]) for s in splited]
taxi_data['year'] = year
taxi_data['month'] = month
taxi_data['day'] = day
taxi_data['hour'] = hour
taxi_data['weekday'] = [dt.date(dt(year=year[i],month=month[i],day=day[i])).weekday()
                        + 1
                        for i in range(len(datetime))]
distance = [LLs2Dist(taxi_data.iloc[i].pickup_latitude,taxi_data.iloc[i].pickup_longitude,taxi_data.iloc[i].dropoff_latitude,taxi_data.iloc[i].dropoff_longitude) for i in range(taxi_data.shape[0])]
taxi_data['distance'] = distance

taxi_data.to_csv(taxi_data_test_path)
taxi_data.to_csv(taxi_data_test_zip_path, compression='gzip',index=False)