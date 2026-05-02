# Student Marks Analyzer

import matplotlib.pyplot as plt

# Step 1: Data (no internet needed)
students = ["Amit", "Neha", "Raj", "Simran", "Karan"]
marks = [78, 85, 62, 90, 55]

# Step 2: Basic Analysis
average_marks = sum(marks) / len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)

print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

# Step 3: Pass/Fail (Pass if >= 60)
print("\nResult:")
for i in range(len(students)):
    if marks[i] >= 60:
        print(students[i], "-> Pass")
    else:
        print(students[i], "-> Fail")

# Step 4: Visualization (Bar Chart)
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()