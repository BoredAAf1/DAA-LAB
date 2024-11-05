import pandas as pd
import random

def generate_csv(filename, num_items=100):
    data = {'Item': [], 'Value': [], 'Weight': [], 'ShelfLife': []}
    for i in range(num_items):
        data['Item'].append(f'Item{i+1}')
        data['Value'].append(random.randint(10, 200))
        data['Weight'].append(random.randint(1, 50))
        data['ShelfLife'].append(random.randint(1, 30))

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Generate 4 CSV files
for i in range(2, 5):
    filename = f'courier_items{i}.csv'
    generate_csv(filename)


