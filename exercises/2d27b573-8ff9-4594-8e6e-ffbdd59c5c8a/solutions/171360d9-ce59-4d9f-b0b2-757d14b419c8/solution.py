from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
diabetes = load_diabetes()

# Split the dataset into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=42)

# Create a Gradient Boosting Regression model with n_estimators=100 and max_depth=3
gbr = GradientBoostingRegressor(n_estimators=100, max_depth=3)

# Fit the model on the training set
gbr.fit(X_train, y_train)

# Predict the target variable for the testing set
y_pred = gbr.predict(X_test)

# Calculate the mean squared error and R-squared score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean squared error:", mse)
print("R-squared score:", r2)
