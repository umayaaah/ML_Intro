#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn import svm
from sklearn.metrics import accuracy_score

def chris_pred(predictions):
    return len([c for c in predictions if c == 1])

def get_preds(answers, pred):
    for x in range(len(answers)):
        print("Email author for #" + str(answers[x]) + " is: " + str(pred[answers[x]]))

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
clf = svm.SVC(kernel="rbf", C=10000)
t0 = time()

clf.fit(features_train, labels_train)
print("Classifier fitted: {0}").format(round(time()-t0,4))
pred = clf.predict(features_test)
print("Classifier predicted: {0}").format(round(time()-t0,4))

#answers = [10, 26, 50]
#get_preds(answers, pred)
print(chris_pred(pred))

acc = accuracy_score(pred, labels_test)
print("Accuracy calculated: {0}").format(round(time()-t0,4))

print("Accuracy score: " + str(acc))



