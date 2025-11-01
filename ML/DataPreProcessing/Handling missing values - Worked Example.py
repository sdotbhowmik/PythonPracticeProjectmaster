#load required librarries
import pandas as pd

#convert your dataset to dataframe
df = pd.read_csv("employees.csv")

#identify and agreegate the missing values in dataset
# print(df.isnull().sum())


#handling missing values
print(df['Age'].fillna(df['Age'].mean()))
print(df['Department'].fillna(df['Department'].mode()[0]))
