#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../../tools/final_project/final_project_dataset.pkl", "r") )
### outlier is the key TOTAL
data_dict.pop("TOTAL", 0)
### other outliers - salary > 1,000,000 and bonus > 5,000,000

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)



### make scatterplot
for salary, bonus in data:
    plt.scatter(salary, bonus)

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

