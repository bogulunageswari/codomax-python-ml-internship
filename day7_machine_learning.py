from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
hours = np.array([[1], [2], [3], [4], [5], [6]])
marks = np.array([35, 45, 50, 60, 70, 80])

# Create the model
model = LinearRegression()

# Train the model
model.fit(hours, marks)

# Predict marks for a student studying 7 hours
prediction = model.predict([[7]])

print("Predicted marks for 7 hours of study:", prediction[0])

# Model information
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)