from sklearn import tree

def DT_classify(features_train, labels_train):
    clf = tree.DecisionTreeClassifier()

    clf = clf.fit(features_train, labels_train)

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