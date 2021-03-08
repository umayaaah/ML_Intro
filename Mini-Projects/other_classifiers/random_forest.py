#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn import ensemble
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
def init_vis():
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()
################################################################################
# 93.6% highest accuracy overall


# 92.4% accuracy
def random_forest():
    clf = ensemble.RandomForestClassifier(n_estimators=1000, max_features="auto", max_depth=3)
    print("Fitting classifier....")
    clf = clf.fit(features_train, labels_train)
    print("Completed fitted classifier.\nMaking predictions....")
    pred = clf.predict(features_test)
    print("Completed making predictions.")
    acc = accuracy_score(pred, labels_test)
    print("Accuracy score: " + str(acc))
    return clf

clf = random_forest()

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
