from sklearn.naive_bayes import GaussianNB
import numpy as np

values = input().strip().split(' ')
x1 = int(values[0])
x2 = int(values[1])

# input data
X = np.array([[1, 0], [1, 1], [0, 1], [0, 0]])
Y = np.array([0, 1, 0, 1])

# create a Naive Bayes classifier
model = GaussianNB()

# fit the model to the data
model.fit(X, Y)

# predict the value of Y
x_pred = np.array([[x1, x2]])
y_pred = model.predict(x_pred)
print(y_pred[0])
