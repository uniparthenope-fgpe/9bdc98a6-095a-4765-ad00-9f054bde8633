from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Create a Gaussian Naive Bayes classifier
gnb = GaussianNB()

# Load iris dataset
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Fit the classifier on the training set
gnb.fit(X_train, y_train)

# Predict the class labels for the testing set
y_pred = gnb.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Print the confusion matrix
print("Confusion matrix:\n", cm)
