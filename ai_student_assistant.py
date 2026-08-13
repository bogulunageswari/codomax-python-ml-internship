print("===== AI STUDENT ASSISTANT =====")

print("1. Study Tips")
print("2. Python Help")
print("3. Study Plan")

choice = input("Choose an option: ")

if choice == "1":
    print("\nStudy Tips:")
    print("- Make a daily study schedule")
    print("- Practice coding every day")
    print("- Take short breaks")
    print("- Revise what you learned")

elif choice == "2":
    print("\nPython Tip:")
    print("Practice variables, loops, functions and problem solving.")

elif choice == "3":
    print("\nSimple Study Plan:")
    print("1 hour - Python")
    print("1 hour - Machine Learning")
    print("30 minutes - Problem Solving")
    print("30 minutes - Revision")

else:
    print("Invalid choice")

print("\nThank you for using AI Student Assistant!")