import pandas as pd

# Step 1: Load data from CSV
data = pd.read_csv("students.csv")

# Step 2: Show data
print("Student Data:\n")
print(data)

# Step 3: Basic Analysis
average = data["Marks"].mean()
highest = data["Marks"].max()
lowest = data["Marks"].min()

print("\nAverage Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Step 4: Pass/Fail
print("\nResults:")
for i in range(len(data)):
    if data["Marks"][i] >= 60:
        print(data["Name"][i], "-> Pass")
    else:
        print(data["Name"][i], "-> Fail")