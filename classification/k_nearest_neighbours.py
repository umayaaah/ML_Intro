from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from scipy.spatial import distance

def euc_distance(x, y):
    return distance.euclidean(x, y)

class MyKNNClassifier():
    def fit(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train

    def predict(self, features_test):
        predictions = []
        for row in features_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc_distance(row, self.features_train[0])
        best_idx = 0
        print("Best distance: " + str(best_dist))
        for i in range(1, len(self.features_train)):
            # print("Best distance: " + str(best_dist))
            dist = euc_distance(row, self.features_train[i])
            # print("New distance: " + str(dist))
            if dist < best_dist:
                print("Improvement! New distance: " + str(dist))
                best_dist = dist
                best_idx = i

        print("Label chosen: " + str(self.labels_train[best_idx]))
        return self.labels_train[best_idx]
        
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
    clf = MyKNNClassifier()

    acc = k_neighbour_classify(clf, X_train, y_train, X_test, y_test)
    print("Accuracy of classfier: " + str(round(acc,3)))

if __name__ == "__main__":
    main()

