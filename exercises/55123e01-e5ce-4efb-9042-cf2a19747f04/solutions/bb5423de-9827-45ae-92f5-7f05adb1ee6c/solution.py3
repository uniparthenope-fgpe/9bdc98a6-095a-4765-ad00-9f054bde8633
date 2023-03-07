import numpy as np
from sklearn.cluster import KMeans

# input data
X = np.array([[2, 3], [3, 2], [3, 4], [4, 3], [8, 9], [9, 8], [9, 10], [10, 9]])

# create a K-Means clustering model with two clusters
kmeans = KMeans(n_clusters=2, n_init='auto')

# fit the model to the data
kmeans.fit(X)

# predict the cluster labels for each data point
labels = kmeans.predict(X)

print(labels)