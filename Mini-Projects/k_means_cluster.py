#!/usr/bin/python 

""" 
    Lesson 9: K-means clustering mini-project.
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ plot graph to visualize clusters """
    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    # plt.show()
    # plt.close()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../tools/final_project/final_project_dataset.pkl", "r") )
### remove total outlier 
data_dict.pop("TOTAL", 0)
### feature scaling - min/max values for exercised_stock_options
# print(data_dict)

def feature_range(feature):
    feature_vals = []
    for person in data_dict:
        feature_vals.append(data_dict[person][feature])

    feature_vals = [x for x in feature_vals if x != "NaN"]
    print("--- Feature range for {0} ---\nMinimum value: {1}\nMaximum value: {2}\n".format(feature, min(feature_vals), max(feature_vals)))

feature_range("exercised_stock_options")
feature_range("salary")

def feature_scaler(feature_arr):
    nozero_arr = np.ma.masked_equal(feature_arr, 0.0, copy=False)
    min_val = np.min(nozero_arr)
    max_val = np.max(nozero_arr)
    if(min_val == max_val):
        return feature_arr
    
    scaled_feature = []
    
    for x in feature_arr:
        x = float(x)
        rescale_x = (x - min_val)/(max_val - min_val)
        scaled_feature.append(rescale_x)
    
    return scaled_feature

feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"

poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

print(finance_features)
# finance_features = feature_scaler(finance_features)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(finance_features)
print(scaler.data_max_)
print(("Scaled value of salary = 200,000 and exercised stock options = 1,000,000: {0}").format(scaler.transform([[200000., 1000000]])))
scaled_data = scaler.transform(finance_features)

### clustering with n features 
for f1, f2 in scaled_data:
    plt.scatter( f1, f2)

# plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans

km = KMeans(n_clusters=2).fit(finance_features)
pred = km.predict(finance_features)



### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="scaled-feature-clusters.png", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
