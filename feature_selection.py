from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def recursiveFeatureElimination(X, Y):
    model = LogisticRegression()
    rfe = RFE(model, 15)
    fit = rfe.fit(X, Y)

def featureExtraction(X, Y):
    model = ExtraTreesClassifier()
    fit = model.fit(X, Y)


def univarientFeatureExtraction(X, Y):
    model = SelectKBest(score_func=chi2, k=15)
    fit = model.fit(X, Y)