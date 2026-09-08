"""
Question: Get a three-digit number from the user and print the sum of all digits.
Test case:
Input: 738 -> Output: 18
"""
surya=int(input("Enter a three-digit number: "))

def sum_of_digits(num):
    if 100 <= num <= 999:
        hundreds = num // 100
        tens = (num // 10) % 10
        units = num % 10
        return hundreds + tens + units
    else:
        return "Error: Please enter a three-digit number."

print("Output:", sum_of_digits(surya))