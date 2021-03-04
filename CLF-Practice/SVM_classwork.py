from sklearn import svm
from sklearn.metrics import accuracy_score

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl

def SVM_classify(features_train, labels_train, features_test, labels_test):
    #features_train, labels_train, features_test, labels_test = makeTerrainData()

    ########################## SVM #################################
    ### SVC creation here
    clf = svm.SVC(kernel="linear")

    #### now your job is to fit the classifier
    #### using the training features/labels, and to
    #### make a set of predictions on the test data
    clf.fit(features_train, labels_train)

    #### store your predictions in a list named pred
    #### you pass in features from test data set for the clf to predict the labels
    pred = clf.predict(features_test)
    acc = accuracy_score(pred, labels_test)

    print(acc)
    return clf

def submitAccuracy():
    return acc

def intro():
    X = [[0,0], [1,1], [2,2]] #training features
    y = [0,1,2] #training labels
    test_features = [[2,2], [3,3]]
    test_labels = [1, 2]
    # classifier
    clf = svm.SVC()
    clf.fit(X, y)

    pred = clf.predict(test_features)
    print(pred)
    score = accuracy_score(pred, test_labels)
    print(score)

