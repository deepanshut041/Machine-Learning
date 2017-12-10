#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
from sklearn.linear_model import LinearRegression
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../tools/final_project_dataset_unix.pkl", "rb") )
data_dict.pop('TOTAL', 0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

raw_data = []
### your code below
for point in data:
	salary = point[0]
	bonus = point[1]
	matplotlib.pyplot.scatter( salary, bonus )
k = 0

# Making new tupel for analysis
for i in data:
	for j in data_dict:
		if data_dict[j]['salary'] == i[0]:
			raw_data.append((k, j, data_dict[j]))
	k = k + 1

# Sorting this according to salary
for i in range(0, len(raw_data), 1):
    for j in range(0, len(raw_data) - 1, 1):   
        if raw_data[j][2]['salary'] > raw_data[j + 1][2]['salary']:
            temp = raw_data[j]
            raw_data[j] = raw_data[j + 1]
            raw_data[j + 1] = temp


# Finding culprit last two of them are culprit
for i in raw_data:
	print(i[0],i[1])
	print()


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


