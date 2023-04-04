from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

iris = load_iris()

pca = PCA(n_components=2)
X_2d = pca.fit_transform(iris.data)
print(X_2d)
