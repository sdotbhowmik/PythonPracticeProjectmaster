import pandas as pd
from pyexpat import features

df = pd.read_csv("students.csv")

print("First 5 row of the dataset")
print(df.head())

features = df[["Age","Salary","Hours_studied"]]
label = df["Passed"]

print("\nFeatures (X)")
print(features.head())

print("\nLabel (y):")
print(label.head())