import pandas as pd

def fractional_knapsack(file_path, capacity=200):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate value-to-weight ratio for each item
    df['value_to_weight'] = df['Value'] / df['Weight']
    
    # Sort by shelf life in ascending order and by value-to-weight ratio in descending order
    df = df.sort_values(by=['ShelfLife', 'value_to_weight'], ascending=[True, False])
    
    total_value = 0
    total_weight = 0
    
    # Iterate over sorted items
    for _, row in df.iterrows():
        if total_weight + row['Weight'] <= capacity:
            # Take the whole item
            total_weight += row['Weight']
            total_value += row['Value']
        else:
            # Take fractional part of the item
            remaining_capacity = capacity - total_weight
            total_value += row['value_to_weight'] * remaining_capacity
            total_weight += remaining_capacity
            break

    return total_value

# Example usage:
file_path = 'courier_items.csv'
max_value = fractional_knapsack(file_path)
print(f"Maximum value achievable within 200 tons capacity: {max_value}")
