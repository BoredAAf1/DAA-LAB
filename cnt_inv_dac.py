import csv
import os

# Function to use a variation of merge sort to count inversions
def merge_and_count(arr):
    if len(arr) < 2:
        return arr, 0
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left, left_inv = merge_and_count(arr[:mid])
    right, right_inv = merge_and_count(arr[mid:])
    
    # Merge and count inversions
    merged, split_inv = merge(left, right)
    
    # Total inversions = inversions in left + inversions in right + split inversions
    total_inversions = left_inv + right_inv + split_inv
    
    return merged, total_inversions

# Merge function to count split inversions
def merge(left, right):
    merged = []
    i = j = 0
    split_inv = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            # Every time we choose an element from the right, it means there are inversions
            split_inv += len(left) - i
    
    # Append the remaining elements of left and right arrays
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, split_inv

# Lists to store students based on their inversion counts
zero_inversions = []
one_inversion = []
two_inversions = []
three_inversions = []

# Read the CSV file
file_path = 'students_with_3_courses_9.csv'

# Check if the file is empty
if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
    print("Error: The CSV file is either missing or empty.")
else:
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Process each student
        for row in reader:
            name = row["Name"]
            
            # Check if the name is missing
            if not name:
                print("Error: Student with missing name found. Skipping this entry.")
                continue
            
            try:
                # Convert course codes to integers and handle invalid values
                courses = [int(row["Course 1"]), int(row["Course 2"]), int(row["Course 3"])]
            except ValueError:
                # Output error message if course is not a number
                print(f"Error: Invalid course code for student '{name}'. Skipping this entry.")
                continue
            
            # Count inversions using merge sort based approach
            _, inversion_count = merge_and_count(courses)
            
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
