from sklearn import linear_model
from class_vis import plot_graph, output_image
import numpy as np
import matplotlib.pyplot as plt
 


def intro():
    clf = linear_model.LinearRegression()
    X_train = np.array([[1],[1.5],[4], [6]])
    y_train = np.array([1.5,2,3, 5])

    X_test = [[0],[2],[3]]
    y_test = [0,2,2.5]
    clf.fit(X_train, y_train)

    getInfo(clf, X_train, y_train, X_test, y_test)

    plt.scatter(X_train, y_train)
    plot_graph(clf, X_train, y_train, X_test, y_test, "X", "y")
    output_image("test.png", "png", open("test.png", "rb").read())

def getInfo(clf, X_train, y_train, X_test, y_test):
    # print("Prediction on " + str(y_test) + ": " + clf.predict([y_test]))
    print("Slope: {0}\nIntercept: {1}".format(clf.coef_, clf.intercept_))
    print("\n ---- Stats on test dataset -----")
    print("r-squared score: {0}".format(clf.score(X_test, y_test)))
    print("\n ---- Stats on trainig dataset -----")
    print("r-squared score: {0}".format(clf.score(X_train, y_train)))


def main():
    intro()

if __name__ == "__main__":
    main()