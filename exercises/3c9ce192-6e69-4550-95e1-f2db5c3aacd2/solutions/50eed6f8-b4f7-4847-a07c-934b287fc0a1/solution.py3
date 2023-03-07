import numpy as np
from sklearn.linear_model import LinearRegression

value = int(input().strip())

# input data
X = np.array([1, 2, 3, 4])
Y = np.array([3, 5, 7, 9])

# reshape the data to make it compatible with scikit-learn
X = X.reshape((-1, 1))

# create a linear regression model
model = LinearRegression()

# fit the model to the data
model.fit(X, Y)

# predict the value of Y for X = 5
x_pred = np.array([[value]])
y_pred = model.predict(x_pred)
print(int(y_pred[0]))
