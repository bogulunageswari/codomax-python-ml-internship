from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Student study hours
hours = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

# 0 = Fail, 1 = Pass
result = np.array([
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1
])

# Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    hours,
    result,
    test_size=0.2,
    random_state=42
)

# Create the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual values:", y_test)
print("Predicted values:", y_pred)
print("Model Accuracy:", accuracy * 100, "%")