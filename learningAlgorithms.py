from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier


def decesionTree(X_train, Y_train):
    dtree = DecisionTreeClassifier()
    return dtree.fit(X_train, Y_train)


def naiveBayes(X_train, Y_train):
    nBayes = MultinomialNB()
    return nBayes.fit(X_train, Y_train)


def adaBoost(X_train, Y_train):
    abc = AdaBoostClassifier(n_estimators=50, learning_rate=1)
    return abc.fit(X_train, Y_train)

