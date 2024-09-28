def arm(number, n):
    total_sum = 0
    a = number  # Use the input number for calculations
    while a > 0:
        rem = a % 10  # Get the last digit
        total_sum += rem ** n  # Add the digit raised to the power of n to total_sum
        a = a // 10  # Remove the last digit
    return total_sum == number  # Check if the sum equals the original number

# Input and function call
a = int(input("Enter the number: "))
n = len(str(a))  # Get the number of digits
if arm(a, n):
    print(f"{a} is an Armstrong number.")
else:
    print(f"{a} is not an Armstrong number.")


    
