def binary_to_decimal(binary_value):
    
    decimal_value = 0
    binary_str = str(binary_value)
    length = len(binary_str)
    
    for i in range(length):
        bit = int(binary_str[length - 1 - i])
        decimal_value += bit * (2 ** i)
    
    return decimal_value

# Example usage
binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print("Decimal value:", decimal_output) 
