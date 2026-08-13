from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data
hours = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
result = np.array([0, 0, 0, 1, 1, 1, 1, 1])

# 0 = Fail
# 1 = Pass

# Create the model
model = LogisticRegression()

# Train the model
model.fit(hours, result)

# Predict for a student who studies 5 hours
prediction = model.predict([[5]])

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

# Probability
probability = model.predict_proba([[5]])

print("Fail probability:", probability[0][0])
print("Pass probability:", probability[0][1])