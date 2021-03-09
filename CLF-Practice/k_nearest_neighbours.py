from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def k_neighbour_classify(clf, features_train, labels_train, features_test, labels_test):
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    accuracy = accuracy_score(pred, labels_test)
    return accuracy

def main():
    iris = datasets.load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    clf = KNeighborsClassifier()

    acc = k_neighbour_classify(clf, X_train, y_train, X_test, y_test)
    print("Accuracy of classfier: " + str(round(acc,3)))

if __name__ == "__main__":
    main()

