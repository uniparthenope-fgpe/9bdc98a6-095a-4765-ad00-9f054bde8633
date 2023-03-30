from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = load_iris()

# Split the dataset into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create an AdaBoost classifier
ada = AdaBoostClassifier(random_state=42)

# Train the model on the training set
ada.fit(X_train, y_train)

# Predict the target variable for the testing set
y_pred = ada.predict(X_test)

# Evaluate the performance of the model on the testing set using the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
