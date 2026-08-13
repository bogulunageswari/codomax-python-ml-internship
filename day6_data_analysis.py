import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("student_data.csv")

print("Student Dataset:")
print(df)

# Basic information
print("\nDataset Information:")
print(df.info())

# Statistics
print("\nStatistics:")
print(df.describe())

# Average marks
print("\nAverage Marks:", df["Marks"].mean())

# Highest marks
print("Highest Marks:", df["Marks"].max())

# Lowest marks
print("Lowest Marks:", df["Marks"].min())

# Student with highest marks
top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Student:")
print(top_student)

# Students scoring above 80
print("\nStudents scoring above 80:")
print(df[df["Marks"] > 80])

# Visualization
plt.bar(df["Name"], df["Marks"])

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()