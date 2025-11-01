# linear_regression_main.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def linear_regression_task(csv_file="students.csv", predict_hours=5, save_plot="regression_plot.png"):
    """
    Performs Linear Regression on a dataset, predicts score, calculates MSE, and plots the regression line.

    Returns:
        predicted_score (float): Predicted score for given hours
        mse (float): Mean Squared Error of the model
    """

    # Step 1: Load the dataset
    df = pd.read_csv(csv_file)

    # Step 2: Define features (X) and target (y)
    X = df[["Hours_Studied"]]
    y = df["Exam_Score"]

    # Step 3: Create the linear regression model
    model = LinearRegression()

    # Step 4: Fit the model
    model.fit(X, y)

    # Step 5: Make prediction
    predicted_score = model.predict([[predict_hours]])[0]
    print(f"Predicted exam score for studying {predict_hours} hours is: {predicted_score}")

    # Step 6: Calculate Mean Squared Error
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    print(f"Mean Squared Error of the model: {mse}")

    # Step 7: Plot the data points and regression line
    plt.scatter(X, y, color="blue", label="Actual Data")
    plt.plot(X, y_pred, color="red", label="Regression Line")
    plt.xlabel("Hours Studied")
    plt.ylabel("Exam Score")
    plt.title("Linear Regression: Exam Score vs Hours Studied")
    plt.legend()
    plt.savefig(save_plot)  # Save the plot as an image
    plt.close()

    return predicted_score, mse


# Main function to run when script is executed directly
if __name__ == "__main__":
    linear_regression_task()