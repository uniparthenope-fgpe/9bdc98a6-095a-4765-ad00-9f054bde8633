import numpy as np
from sklearn.linear_model import LogisticRegression

values = input().strip().split(' ')
x1 = int(values[0])
x2 = int(values[1])

# input data
X1 = np.array([1, 2, 3, 4])
X2 = np.array([2, 1, 4, 3])
Y = np.array([0, 0, 1, 1])

# create a logistic regression model
model = LogisticRegression()

# fit the model to the data
X = np.column_stack((X1, X2))
model.fit(X, Y)

# predict the value of Y
x_pred = np.array([[x1, x2]])
y_pred = model.predict(x_pred)
print(y_pred[0])
