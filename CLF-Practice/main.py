from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from NB_classwork import NB_classify
from SVM_classwork import SVM_classify
from DT_classwork import DT_classify


import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
def classifyNB():
    # clf = classify(features_train, labels_train, features_test, labels_test)

    clf = NB_classify(features_train, labels_train, features_test, labels_test)

    ### draw the decision boundary with the text points overlaid
    prettyPicture(clf, features_test, labels_test)
    output_image("test.png", "png", open("test.png", "rb").read())

def classifySVM():
    # clf = classify(features_train, labels_train, features_test, labels_test)

    clf = SVM_classify(features_train, labels_train, features_test, labels_test)

    ### draw the decision boundary with the text points overlaid
    prettyPicture(clf, features_test, labels_test)
    output_image("test.png", "png", open("test.png", "rb").read())

def classifyDT(features_train, labels_train):
    clf = DT_classify(features_train, labels_train)
    prettyPicture(clf, features_test, labels_test)
    output_image("tree.png", "png", open("test.png", "rb").read())

classifyDT(features_train, labels_train)