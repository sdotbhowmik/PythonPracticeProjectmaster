import math
from sklearn.metrics import mean_squared_error

#step1: Actual vs Predicted values
y_true = [50, 60, 70, 80]
y_predicted = [48, 65, 68, 75]

#step2: calculate MSE
mse = mean_squared_error(y_true,y_predicted)
print("MSE: ", mse)

#step3: calculate RMSE
rmse = math.sqrt(mse)

print("Mean Squared Error (MSE): ", round(mse,2))
print("Root Mean Squared Error (RMSE): ",round(rmse,2))