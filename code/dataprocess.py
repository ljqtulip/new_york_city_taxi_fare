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

# # lon_min, lon_max = -75, -72
# # lat_min, lat_max = 40, 43
# lon_min, lon_max = -180, 180
# lat_min, lat_max = -90, 90
# taxi_file_path = 'datas/new_york_city_taxi_fare_prediction/train.csv'
# taxi_data_train_path = 'datas/prepare/train.csv'
# taxi_data = pd.read_csv(taxi_file_path,nrows=1000000)
# print(taxi_data.shape)
# #drop the missing data
# taxi_data = taxi_data.drop(taxi_data[taxi_data.isnull().any(1)].index, axis = 0)
# #drop unexpected values
# taxi_data = taxi_data.drop(taxi_data[taxi_data['fare_amount']<=0].index, axis=0)
# taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==208].index, axis = 0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']<lat_min]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']>lat_max]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']<lon_min]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']>lon_max]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']<lat_min]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']>lat_max]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']<lon_min]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']>lon_max]).index, axis=0)
#
# print(taxi_data.shape[0])
# distance = [LLs2Dist(taxi_data.iloc[i].pickup_latitude,taxi_data.iloc[i].pickup_longitude,taxi_data.iloc[i].dropoff_latitude,taxi_data.iloc[i].dropoff_longitude) for i in range(taxi_data.shape[0])]
# taxi_data['distance'] = distance
#
# # taxi_data_train_path = 'datas/prepare/train.csv'
# # taxi_data = pd.read_csv(taxi_data_train_path)
# # unit_price = [taxi_data.iloc[i].fare_amount/taxi_data.iloc[i].distance for i in range(taxi_data.shape[0])]

taxi_data_source = '../datas/prepare/clean.csv'
taxi_data_train_path = '../datas/prepare/train.csv'
taxi_data_train_zip_path = '../data_zipped/train.gz'
taxi_data = pd.read_csv(taxi_data_source)
datetime = taxi_data.pickup_datetime
print(datetime)
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

for i in range(taxi_data.shape[0]):
    data = taxi_data.iloc[i]
    if data.distance > 200 and data.fare_amount > 2.5:
        taxi_data.iloc[i].distance = (data.fare_amount-2.5)/1.56
    if data.fare_amount == 0 and data.distance == 0:
        taxi_data.drop(i)
    if data.fare_amount !=0 and data.fare_amount < 2.5 and data.distance == 0:
        taxi_data.drop(i)
    if data.fare_amount == 0 and distance != 0:
        taxi_data.iloc[i].fare_amount = 2.5+1.56*data.distance


#data saving
taxi_data.to_csv(taxi_data_train_path)
taxi_data.to_csv(taxi_data_train_zip_path, compression='gzip',index=False)
