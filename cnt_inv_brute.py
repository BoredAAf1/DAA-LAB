import csv

# Function to count the number of inversions in a list of courses
def count_inversions(courses):
    inversions = 0
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            if courses[i] > courses[j]:
                inversions += 1
    return inversions

# Lists to store students based on their inversion counts
zero_inversions = []
one_inversion = []
two_inversions = []
three_inversions = []

# Read the CSV file
file_path = 'students_with_3_courses.csv'
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    
    # Process each student
    for row in reader:
        name = row["Name"]
        courses = [int(row["Course 1"]), int(row["Course 2"]), int(row["Course 3"])]
        
        # Count inversions in the student's course list
        inversion_count = count_inversions(courses)
        
        # Categorize the student based on their inversion count
        if inversion_count == 0:
            zero_inversions.append(name)
        elif inversion_count == 1:
            one_inversion.append(name)
        elif inversion_count == 2:
            two_inversions.append(name)
        elif inversion_count == 3:
            three_inversions.append(name)

# Output the categorized lists of student names
print("Students with 0 inversions:", zero_inversions)
print("Students with 1 inversion:", one_inversion)
print("Students with 2 inversions:", two_inversions)
print("Students with 3 inversions:", three_inversions)
