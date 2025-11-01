import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("employees.csv")

#look at slary columns different properties
print(df['Salary'].describe())

#visualize and save as image
plt.boxplot(df['Salary'])
plt.title("Salary Distribution with Outliers")
plt.savefig('salary_outliers.png')


#setting outliers rule
outliers = df[(df['Salary'] < 10000) | (df['Salary'] > 20000)]
print("Outliers Found:\n", outliers)

#removing the outliers
df_clean = df[(df['Salary']>= 10000) & (df['Salary']<=200000)]

print("Dataset shape before:", df.shape)
print("Dataset shape after removing outliers:", df_clean.shape)