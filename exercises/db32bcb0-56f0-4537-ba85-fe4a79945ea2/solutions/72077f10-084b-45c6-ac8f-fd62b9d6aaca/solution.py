from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier

wine = load_wine()
X = wine.data
y = wine.target

clf = DecisionTreeClassifier(criterion='entropy')
clf.fit(X, y)
