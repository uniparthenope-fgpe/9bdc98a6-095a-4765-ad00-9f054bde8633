import numpy as np
from sklearn.linear_model import LinearRegression

value = int(input().strip())

# input data
X = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500])
Y = np.array([50, 75, 100, 125, 150, 175, 200, 225, 250, 275])

# reshape the data to make it compatible with scikit-learn
X = X.reshape((-1, 1))

# create a linear regression model
model = LinearRegression()

# fit the model to the data
model.fit(X, Y)

# predict the value of Y
x_pred = np.array([[value]])
y_pred = model.predict(x_pred)
print(int(y_pred[0]))

