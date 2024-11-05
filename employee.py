import pandas as pd
import sys
class Employee:
    def __init__(self, name, base, HRA, income_tax, provident_fund, deductions):
        self.name = name
        self.base = base
        self.HRA = HRA
        self.income_tax = income_tax
        self.provident_fund = provident_fund
        self.deductions = deductions

    def gross_salary(self):
        return self.base + self.HRA + self.provident_fund

    def net_salary(self):
        return round(((self.base + self.HRA) * (100 - self.income_tax) / 100) - self.provident_fund - self.deductions, 2)

csv_file = "employee_details1.csv"
try:
    df = pd.read_csv(csv_file)
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty or has no columns")
    sys.exit(1)
gross_salaries = []
net_salaries = []

for index, row in df.iterrows():
    try:
        if pd.isna(row['name']) or pd.isna(row['base']) or row['base'] < 0:
            raise ValueError(f"Invalid data at row {index}: missing or negative base salary")
        if pd.isna(row['HRA']) or row['HRA'] < 0:
            raise ValueError(f"Invalid data at row {index}: missing or negative HRA")
        if pd.isna(row['income_tax']) or row['income_tax'] < 0:
            raise ValueError(f"Invalid data at row {index}: missing or negative income tax percentage")
        if pd.isna(row['provident_fund']) or row['provident_fund'] < 0:
            raise ValueError(f"Invalid data at row {index}: missing or negative provident fund")
        if pd.isna(row['deductions']) or row['deductions'] < 0:
            raise ValueError(f"Invalid data at row {index}: missing or negative deductions")
        name = row['name']
        base = row['base']
        HRA = row['HRA']
        income_tax = row['income_tax']
        provident_fund = row['provident_fund']
        deductions = row['deductions']
        emp = Employee(name, base, HRA, income_tax, provident_fund, deductions)
        gross_salaries.append(emp.gross_salary())
        net_salaries.append(emp.net_salary())
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def find_min_max_iterative(arr):
    if not arr:
        return None, None
    min_val = float('inf')
    max_val = float('-inf')
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

def find_min_max_divide_conquer(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    mid = (low + high) // 2
    min1, max1 = find_min_max_divide_conquer(arr, low, mid)
    min2, max2 = find_min_max_divide_conquer(arr, mid + 1, high)
    return min(min1, min2), max(max1, max2)


min_gross_iter, max_gross_iter = find_min_max_iterative(gross_salaries)
min_net_iter, max_net_iter = find_min_max_iterative(net_salaries)

min_gross_divide, max_gross_divide = find_min_max_divide_conquer(gross_salaries, 0, len(gross_salaries) - 1)
min_net_divide, max_net_divide = find_min_max_divide_conquer(net_salaries, 0, len(net_salaries) - 1)

# Print results
print(f"Iterative Method - Gross Salary: Min: {min_gross_iter}, Max: {max_gross_iter}")
print(f"Divide and Conquer Method - Gross Salary: Min: {min_gross_divide}, Max: {max_gross_divide}")

print(f"Iterative Method - Net Salary: Min: {min_net_iter}, Max: {max_net_iter}")
print(f"Divide and Conquer Method - Net Salary: Min: {min_net_divide}, Max: {max_net_divide}")

