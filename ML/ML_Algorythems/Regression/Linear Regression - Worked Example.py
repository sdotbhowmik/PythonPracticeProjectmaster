from sklearn.linear_model import LinearRegression

#step1: Preparing data
hours = [[1],[2],[3],[4]]
score = [40,50,65,70]

#step2: creating the model
model = LinearRegression()

#step3: training the model
model.fit(hours,score)

#step4: making predictions
predicted_score = model.predict([[3.5]])
print(predicted_score) # Output: [66] (approx)