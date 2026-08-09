import pandas as pd

# Create student data
data = {
    "Name": ["Nageswari", "Rahul", "Priya", "Arjun", "Sneha"],
    "Marks": [85, 78, 92, 67, 88],
    "Age": [20, 21, 20, 22, 21]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Display first rows
print("\nFirst 3 students:")
print(df.head(3))

# Basic information
print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())

# Students who scored more than 80
print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])