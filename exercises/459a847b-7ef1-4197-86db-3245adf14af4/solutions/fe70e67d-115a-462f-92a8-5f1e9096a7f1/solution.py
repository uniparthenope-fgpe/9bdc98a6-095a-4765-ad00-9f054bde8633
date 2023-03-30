from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()

# Create a PCA model with n_components=2
pca = PCA(n_components=2)

# Fit the model on the data
X_pca = pca.fit_transform(iris.data)

print(X_pca)
