from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()

# Create a Decision Tree classifier
clf = DecisionTreeClassifier()

# Calculate the cross-validation score using 5-fold cross-validation
scores = cross_val_score(clf, iris.data, iris.target, cv=5)

# Print the cross-validation scores
print("Cross-validation scores:", scores)
