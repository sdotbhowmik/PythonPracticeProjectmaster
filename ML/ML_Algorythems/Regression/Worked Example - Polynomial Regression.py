import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#step1: prepare data
experience = [[1], [2], [3], [5], [7], [10]]   # Years of experience
salary = [30, 35, 50, 80, 95, 105]            # Salary (in $1000s)

#step2: transfrom features to polynomial features
poly = PolynomialFeatures(degree=2)
experience_poly = poly.fit_transform(experience)

#step3: Create and train the model
model = LinearRegression()
model.fit(experience_poly,salary)

#step4: make predictions
predicted_salary = model.predict(poly.transform([[6]]))
print(predicted_salary) #output[~85]