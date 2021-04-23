from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error
import math
import numpy as np
from sklearn.tree import export_graphviz
from subprocess import call
import graphviz
import os

os.environ['PATH'] = os.pathsep + r'D:\graphviz\graphviz\bin'
pd.options.mode.chained_assignment = None

train_data_path = '../datas/prepare/train.csv'
train_data = pd.read_csv(train_data_path)


y_train = train_data.fare_amount
taxi_features = ['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','distance','year','weekday','hour']
X_train = train_data[taxi_features]
regr = RandomForestRegressor(n_estimators=100,max_depth=30, n_jobs=-1)
regr.fit(X_train,y_train)

# test_data_path = '../datas/prepare/test.csv'
# test_data = pd.read_csv(test_data_path)
# X_test = test_data[taxi_features]
# y_test = test_data.fare_amount
# y_predict = regr.predict(X_test)
# RMSE = math.sqrt(mean_squared_error(y_predict,y_test))
# print(RMSE)

final_data_path = '../datas/prepare/final.csv'
result_path = '../datas/result.csv'
final_data = pd.read_csv(final_data_path)
X_result = final_data[taxi_features]
y_submission = regr.predict(X_result)
print(y_submission)
result = pd.DataFrame(final_data.loc[:, 'key'])
result['fare_amount'] = y_submission
result.to_csv(result_path)

importances = regr.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, taxi_features[indices[f]], importances[indices[f]]))

# print(regr.estimators_.__len__())
# estimator = regr.estimators_[5]
# # export_graphviz(estimator,
# #                 out_file='../model_pic/tree.dot',
# #                 feature_names = taxi_features,
# #                 rounded = True, proportion = False,
# #                 precision = 2, filled = True)
# dot_data = export_graphviz(estimator, out_file=None)
# graph = graphviz.Source(dot_data)
# graph.render('../model_pic/5')
