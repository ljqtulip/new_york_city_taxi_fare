import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz
from sklearn import tree
#import graphviz
import numpy as np
from sklearn.metrics import mean_squared_error

train_data_path = '../datas/prepare/train.csv'
train_data = pd.read_csv(train_data_path)


y_train = train_data.fare_amount
taxi_features = ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','distance']
X_train = train_data[taxi_features]
# X_train = X[:799999]
# y_train = y[:799999]
# X_test = X[800000:]
# y_test = y[800000:]
taxi_model = DecisionTreeRegressor(random_state=1)
taxi_model.fit(X_train,y_train)
# dot_data = tree.export_graphviz(taxi_model,out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render(r'D:\pic\taxi_fare_tree')

test_data_path = 'datas/prepare/test.csv'
test_data = pd.read_csv(test_data_path)
X_test = test_data[taxi_features]
y_test = test_data.fare_amount
y_predict = taxi_model.predict(X_test)
y_error = abs(y_predict-y_test)
# error_rate = y_error/y_test
# avg_error_rate = np.average(error_rate)
# print(error_rate)
# print(avg_error_rate)
RMSE = mean_squared_error(y_predict,y_test)
print(RMSE)