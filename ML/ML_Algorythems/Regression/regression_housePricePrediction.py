# Step 1: Importing necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 2: Creating sample data
# Features: Size (sq ft), Bedrooms, Age (years)
# Target: Price of house in dollars

data = {
    'Size': [1000, 1500, 1200, 2000, 850],
    'Bedrooms': [2, 3, 2, 4, 2],
    'Age': [5, 10, 8, 1, 15],
    'Price': [150000, 200000, 180000, 300000, 120000]  # Target
}

# Converting data to DataFrame
df = pd.DataFrame(data)

# Step 3: Define features (X) and target variable (y)
X = df[['Size', 'Bedrooms', 'Age']]  # Features
y = df['Price']  # Target

# Step 4: Split the data into training and validation sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions on the test set
y_pred = model.predict(X_test)

# Step 7: Evaluate the model
mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error
r2 = r2_score(y_test, y_pred)  # R^2 score

# Output results
print("Model Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Optional: Compare predictions with actual values
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("\nActual vs Predicted:\n", comparison)

# We evaluate the model using two metrics:
# Mean Squared Error (MSE): Measures the average squared difference between the
# actual and predicted values.
# R² Score: Measures how well the regression line approximates
# the real data points (0-1 scale, where 1 is perfect).

# Step 8: Visualize the results
plt.figure(figsize=(10, 6))  # Set up a plotting figure with a width of 10 inches and a height of 6 inches

# Create the scatter plot
plt.scatter(y_test, y_pred, alpha=0.5)  
# Line representing perfect prediction
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)  
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted House Prices')
plt.show()