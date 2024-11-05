def manual_multiply(num1, num2):
    # Convert numbers to strings for easier manipulation
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Store the results of each digit multiplication
    results = []
    
    # Loop through each digit in the second number
    for i in range(len(str_num2)):
        digit = int(str_num2[-(i + 1)])  # Get the current digit from the right
        temp_result = str_num1 + '0' * i  # Prepare the temporary result
        
        # Multiply each digit of num1 by the current digit of num2
        carry = 0
        temp_result_digits = []
        
        for j in range(len(str_num1)-1, -1, -1):
            product = digit * int(str_num1[j]) + carry
            temp_result_digits.append(product % 10)  # Get the last digit
            carry = product // 10  # Get the carry for the next digit
        
        # If there's a carry left, add it to the result
        while carry > 0:
            temp_result_digits.append(carry % 10)
            carry //= 10
        
        # Since we constructed the result in reverse, we need to reverse it
        temp_result_digits.reverse()
        
        # Convert list of digits back to string
        results.append(''.join(map(str, temp_result_digits)))
    
    # Now add the results together
    final_result = 0
    for index, value in enumerate(results):
        final_result += int(value) * (10 ** index)
    
    return final_result

# Input numbers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Multiply the numbers
product = manual_multiply(num1, num2)

# Output the result
print(f"The product of {num1} and {num2} is: {product}")
