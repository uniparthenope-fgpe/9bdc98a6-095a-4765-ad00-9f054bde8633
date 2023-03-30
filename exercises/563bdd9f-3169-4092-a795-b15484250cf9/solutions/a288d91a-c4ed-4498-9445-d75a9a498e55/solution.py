from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Create a K-Means clustering model with 3 clusters (since we know there are 3 classes in the iris dataset)
kmeans = KMeans(n_clusters=3, n_init=10)

# Fit the model on the training set
kmeans.fit(X_train)

# Predict the clusters for the testing set
y_pred = kmeans.predict(X_test)
print("Predicted clusters:", y_pred)
