import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

fig_path = '../figs'
pd.set_option('display.width', 1000)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#
# # taxi_file_path = 'datas/new_york_city_taxi_fare_prediction/train.csv'
# # taxi_data = pd.read_csv(taxi_file_path,nrows=1000000)
# # print(taxi_data.shape)
# # #drop the missing data
# # taxi_data = taxi_data.drop(taxi_data[taxi_data.isnull().any(1)].index, axis = 0)
# # #drop unexpected values
# # taxi_data = taxi_data.drop(taxi_data[taxi_data['fare_amount']<=0].index, axis=0)
# # taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==208].index, axis = 0)
# # taxi_data = taxi_data.drop(taxi_data[taxi_data['passenger_count']==0].index, axis = 0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']<-90]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_latitude']>90]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']<-180]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['pickup_longitude']>180]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']<-90]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_latitude']>90]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']<-90]).index, axis=0)
# # taxi_data = taxi_data.drop((taxi_data[taxi_data['dropoff_longitude']>90]).index, axis=0)
# #
# #
# # y = taxi_data.fare_amount
# # X = taxi_data['passenger_count']
# #
# # plt.scatter(X,y,alpha=0.5)
# # plt.show()
# #
# # X = taxi_data['pickup_longitude']
# # plt.scatter(X,y,alpha=0.5)
# # plt.show()
# #
# # X = taxi_data['dropoff_longitude']
# # plt.scatter(X,y,alpha=0.5)
# # plt.show()
# #
# # X = taxi_data['pickup_latitude']
# # plt.scatter(X,y,alpha=0.5)
# # plt.show()
# #
# # X = taxi_data['dropoff_latitude']
# # plt.scatter(X,y,alpha=0.5)
# # plt.show()
#
# train_data_path = 'datas/prepare/train.csv'
# train_data = pd.read_csv(train_data_path)
#
# print(train_data.corr())
# #sns.heatmap(train_data.corr(),cmap='Blues', annot=True)

train_data_path = '../datas/prepare/train.csv'
test_data_path = '../datas/prepare/test.csv'
train = pd.read_csv(train_data_path)
test = pd.read_csv(test_data_path)
labels = ['fare_amount','pickup_datetime','pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','year','month','day','hour','weekday','distance']
train = pd.DataFrame(train,columns=labels)

train[train['fare_amount'] < 100].fare_amount.hist(bins=100,figsize = (16,8))
plt.xlabel("Fare Amount")
plt.ylabel("Frequency")
plt.savefig('../figs/fare_amount_frequency.png')
plt.show()

city_long_border = (-74.03, -73.75)
city_lat_border = (40.63, 40.85)
fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True)
ax[0].scatter(train['pickup_longitude'].values[:100000], train['pickup_latitude'].values[:100000],
              color='blue', s=1, label='train', alpha=0.1)
ax[1].scatter(test['pickup_longitude'].values[:100000], test['pickup_latitude'].values[:100000],
              color='green', s=1, label='test', alpha=0.1)
fig.suptitle('Train and test area complete overlap.')
ax[0].legend(loc=0)
ax[0].set_ylabel('latitude')
ax[0].set_xlabel('longitude')
ax[1].set_xlabel('longitude')
ax[1].legend(loc=0)
plt.ylim(city_lat_border)
plt.xlim(city_long_border)
plt.savefig('../figs/pickup_postions.png')
plt.show()

# corr = train.corr()
# print(corr)
# sns.heatmap(corr,cmap='Blues', annot=True)
# plt.show()

source = train[np.logical_and(train['distance'] < 200,train['fare_amount'] < 100)]
X = source['distance']
y = source['fare_amount']
plt.scatter(X,y,alpha=0.1)
plt.savefig('../figs/distance_fare.png')
plt.show()