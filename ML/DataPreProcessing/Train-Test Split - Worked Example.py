import pandas as pd
from sklearn.model_selection import train_test_split

#step1: load dataset
df = pd.read_csv('students.csv')

#step2: Features(Age,Marks) and Label(Passed)
x = df[['Age','Marks']]
y = df['Passed']

#step3: split data into training(80%) and testing(20%) set
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=42)

#Step4: Print the results
print("Training set:")
print(X_train)
print(y_train)

print("\nTesting set:")
print(X_test)
print(y_test)

