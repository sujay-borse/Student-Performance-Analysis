
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# Calculate Total and Average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Basic Statistics
highest = df["Average"].max()
lowest = df["Average"].min()
overall_avg = np.mean(df["Average"])

# Pass/Fail (Pass if average >= 40)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")
pass_percentage = (df["Result"].value_counts()["Pass"] / len(df)) * 100

print("Highest Average:", highest)
print("Lowest Average:", lowest)
print("Overall Class Average:", overall_avg)
print("Pass Percentage:", pass_percentage)

# Bar Chart - Student Average Marks
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.savefig("average_marks_bar_chart.png")
plt.close()

# Pie Chart - Pass vs Fail
result_counts = df["Result"].value_counts()
plt.figure()
plt.pie(result_counts, labels=result_counts.index, autopct="%1.1f%%")
plt.title("Pass vs Fail Distribution")
plt.savefig("pass_fail_pie_chart.png")
plt.close()

print("Charts generated successfully!")
