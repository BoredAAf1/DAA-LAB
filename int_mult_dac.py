def karatsuba(x, y):
    # Base case for recursion
    if x < 10 or y < 10:
        return x * y

    # Calculate the size of the numbers
    m = max(len(str(x)), len(str(y)))
    half = m // 2

    # Split x and y into halves
    high_x, low_x = divmod(x, 10**half)
    high_y, low_y = divmod(y, 10**half)
    # Recursive calls to the three multiplications
    z0 = karatsuba(low_x, low_y)        # low_x * low_y
    z1 = karatsuba((low_x + high_x), (low_y + high_y))  # (low_x + high_x) * (low_y + high_y)
    z2 = karatsuba(high_x, high_y)      # high_x * high_y

    # Apply the Karatsuba formula
    return (z2 * (10 ** (2 * half))) + ((z1 - z2 - z0) * (10 ** half)) + z0

# Input numbers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Multiply the numbers using Karatsuba algorithm
product = karatsuba(num1, num2)

# Output the result
print(f"The product of {num1} and {num2} is: {product}")
