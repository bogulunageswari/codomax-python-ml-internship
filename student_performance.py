import numpy as np
from sklearn.linear_model import LogisticRegression

print("======================================")
print(" STUDENT PERFORMANCE PREDICTION SYSTEM")
print("======================================")

# Training data
# [Study Hours, Attendance, Previous Marks]
X = np.array([
    [2, 60, 45],
    [3, 65, 50],
    [4, 70, 55],
    [5, 75, 60],
    [6, 80, 65],
    [7, 85, 70],
    [8, 90, 80],
    [9, 95, 85],
    [10, 98, 90]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1])

# Create and train model
model = LogisticRegression()
model.fit(X, y)

# Get student details
name = input("\nEnter student name: ")
study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_marks = float(input("Enter previous marks: "))

# Prediction
student = np.array([[study_hours, attendance, previous_marks]])
prediction = model.predict(student)

print("\n========== RESULT ==========")
print("Student Name:", name)

if prediction[0] == 1:
    print("Prediction: PASS")
    print("Recommendation: Keep up the good work!")
else:
    print("Prediction: FAIL")
    print("Recommendation: Increase study time and attendance.")

print("============================")