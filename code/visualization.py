import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

pd.set_option('display.width', 1000)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

# taxi_file_path = 'datas/new_york_city_taxi_fare_prediction/train.csv'
# taxi_data = pd.read_csv(taxi_file_path,nrows=1000000)
# print(taxi_data.shape)
# #drop the missing data
# taxi_data = taxi_data.drop(taxi_data[taxi_data.isnull().any(1)].index, axis = 0)
# #drop unexpected values
# taxi_data = taxi_data.drop(taxi_data[taxi_data['fare_amount']<=0].index, axis=0)
# taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==208].index, axis = 0)
# taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==0].index, axis = 0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']<-90]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']>90]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']<-180]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']>180]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']<-90]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']>90]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']<-90]).index, axis=0)
# taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']>90]).index, axis=0)
#
#
# y = taxi_data.fare_amount
# X = taxi_data['passenger_count']
#
# plt.scatter(X,y,alpha=0.5)
# plt.show()
#
# X = taxi_data['pickup_longitude']
# plt.scatter(X,y,alpha=0.5)
# plt.show()
#
# X = taxi_data['dropoff_longitude']
# plt.scatter(X,y,alpha=0.5)
# plt.show()
#
# X = taxi_data['pickup_latitude']
# plt.scatter(X,y,alpha=0.5)
# plt.show()
#
# X = taxi_data['dropoff_latitude']
# plt.scatter(X,y,alpha=0.5)
# plt.show()

train_data_path = 'datas/prepare/train.csv'
train_data = pd.read_csv(train_data_path)

print(train_data.corr())
#sns.heatmap(train_data.corr(),cmap='Blues', annot=True)