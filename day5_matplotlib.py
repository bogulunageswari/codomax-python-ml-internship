import matplotlib.pyplot as plt

# Student data
names = ["Nageswari", "Rahul", "Priya", "Arjun", "Sneha"]
marks = [85, 78, 92, 67, 88]

# Create bar chart
plt.bar(names, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()