from sklearn.tree import DecisionTreeClassifier

# Training data
# Study hours
X = [[1], [2], [3], [4], [5], [6], [7], [8]]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1, 1, 1]

# Create the model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, y)

# Predict for a new student
hours = [[5]]
prediction = model.predict(hours)

if prediction[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")