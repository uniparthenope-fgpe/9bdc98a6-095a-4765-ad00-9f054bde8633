from sklearn.tree import DecisionTreeClassifier
import numpy as np

values = input().strip().split(' ')
x1 = int(values[0])
x2 = int(values[1])
x3 = int(values[2])

# input data
X = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 1], [0, 1, 0]])
Y = np.array([0, 0, 0, 1, 1, 1])

# create a decision tree model
model = DecisionTreeClassifier()

# fit the model to the data
model.fit(X, Y)

# predict the value of Y
x_pred = np.array([[0, 0, 1]])

y_pred = model.predict(x_pred)
print(y_pred[0])
