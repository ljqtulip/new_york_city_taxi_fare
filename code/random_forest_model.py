from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error
import math

train_data_path = '../datas/prepare/train.csv'
train_data = pd.read_csv(train_data_path)


y_train = train_data.fare_amount
taxi_features = ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','distance','year','weekday','hour']
X_train = train_data[taxi_features]
# X_train = X[:799999]
# y_train = y[:799999]
# X_test = X[800000:]
# y_test = y[800000:]
regr = RandomForestRegressor(n_estimators=100,max_depth=30, n_jobs=-1)
regr.fit(X_train,y_train)

test_data_path = '../datas/prepare/test.csv'
test_data = pd.read_csv(test_data_path)
X_test = test_data[taxi_features]
y_test = test_data.fare_amount
y_predict = regr.predict(X_test)
RMSE = math.sqrt(mean_squared_error(y_predict,y_test))
print(RMSE)

# final_data_path = 'datas/prepare/final.csv'
# result_path = 'datas/result.csv'
# final_data = pd.read_csv(final_data_path)
# X_result = final_data[taxi_features]
# y_submission = regr.predict(X_result)
# X_result['fare_amount'] = y_submission
# result = X_result[["key", "fare_amount"]]
# # y_submission = pd.DataFrame(y_submission,columns=['fare_amount'])
# # result = pd.concat([X_result[['key']],y_submission])
# result.to_csv(result_path)