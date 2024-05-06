##cell1
# Import the required pandas library
import pandas as pd

# Initialize a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['Sales', 'Marketing', 'Sales', 'IT', 'Marketing'],
    'Salary': [48000, 52000, 47000, 61000, 56000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Initial DataFrame:")
print(df)
##

##cell2
# Analyze basic statistics of numerical columns
print("\nBasic Stats:")
print(df.describe())
##

##cell3
# Calculate the average salary per department
avg_salary_per_dept = df.groupby('Department')['Salary'].mean()

print("\nAverage Salary per Department:")
print(avg_salary_per_dept)
##

##cell4
# Add a new column to calculate adjusted salaries with a 5% increase
df['Adjusted Salary'] = df['Salary'] * 1.05

print("\nDataFrame with Adjusted Salaries:")
print(df)
##

##cell5
# Filter out employees older than 25 and create a subset DataFrame
older_than_25 = df[df['Age'] > 25]

print("\nSubset of Employees Older Than 25:")
print(older_than_25)
##

##cell6
# Generate a final summary report
summary_report = {
    "Total Employees": len(df),
    "Average Age": df['Age'].mean(),
    "Departments": df['Department'].unique().tolist(),
    "Highest Salary": df['Salary'].max(),
    "Lowest Salary": df['Salary'].min(),
    "Average Salary": df['Salary'].mean(),
    "Average Salary per Department": avg_salary_per_dept.to_dict()
}

print("\nSummary Report:")
print(summary_report)
##
