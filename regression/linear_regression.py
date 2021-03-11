from sklearn import linear_model


def intro():
    clf = linear_model.LinearRegression()
    clf.fit([[0,0],[1,1],[2,2]], [0,1,2])
    print(clf.coef_)

def main():
    intro()

if __name__ == "__main__":
    main()