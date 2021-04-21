import pandas as pd

# lon_min, lon_max = -75, -72
# lat_min, lat_max = 40, 43
lon_min, lon_max = -180, 180
lat_min, lat_max = -90, 90
taxi_file_path = '../datas/new_york_city_taxi_fare_prediction/train.csv'
taxi_data_clean_path = '../datas/prepare/clean.csv'
taxi_data_clean_zip_path = '../data_zipped/clean.gz'
taxi_data = pd.read_csv(taxi_file_path,nrows=1000000)
print(taxi_data.shape)
#drop the missing data
taxi_data = taxi_data.drop(taxi_data[taxi_data.isnull().any(1)].index, axis = 0)
#drop unexpected values
taxi_data = taxi_data.drop(taxi_data[taxi_data['fare_amount']<0].index, axis=0)
taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==208].index, axis = 0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']<lat_min]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']>lat_max]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']<lon_min]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']>lon_max]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']<lat_min]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']>lat_max]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']<lon_min]).index, axis=0)
taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']>lon_max]).index, axis=0)

taxi_data.to_csv(taxi_data_clean_path)
taxi_data.to_csv(taxi_data_clean_zip_path, compression='gzip',index=False)