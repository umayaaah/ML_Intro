from sklearn import tree
from sklearn.metrics import accuracy_score

def DT_classify(features_train, labels_train, features_test, labels_test):
    # min_sample_split = 2: 0.908 accuracy
    # min_sample_split = 50: 0.912 accuracy
    clf = tree.DecisionTreeClassifier(min_samples_split=50, criterion="entropy")

    clf = clf.fit(features_train, labels_train)

    pred = clf.predict(features_test)
    acc = accuracy_score(pred, labels_test)

    print(acc)

    return clf



def fruit():
    # [weight, {bumpy=0, smooth=1}]
    features = [[140, 1], [130, 1], [150, 0], [170, 0]]
    # output for corresponding feature {apple=0, orange=1}
    labels = [0, 0, 1, 1]

    # decision tree classifier
    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(features, labels)

    # predict label for features: 150kg and bumpy
    pred = clf.predict([[150, 0]]) 

    # prints [1], which is an orange
    print(pred)


def intro():
    X = [[0,0], [1,1]]
    Y = [0,1]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    pred = clf.predict([[2,2]])
    print(pred)