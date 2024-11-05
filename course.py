import csv
import random

# File path for the CSV file
file_path = 'students_with_3_courses_5.csv'

# Generate student names
names = [f"Student_{i}" for i in range(1, 101)]

# Courses limited to 1001, 1002, 1003
limited_courses = [1001, 1002, 1003]

# Generate student data with 3 unique courses per student
students_with_3_courses = [
    {
        "Name": names[i],
        "Number": i + 1,
        "Course 1": random.choice(limited_courses),
        "Course 2": random.choice(limited_courses),
        "Course 3": random.choice(limited_courses)
    }
    for i in range(100)
]

# Write the data to a CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Number", "Course 1", "Course 2", "Course 3"])
    writer.writeheader()
    writer.writerows(students_with_3_courses)

print(f"CSV file '{file_path}' created successfully.")
