"""
Question: Get a two-digit number from the user and print the sum of all digits.
Test case:
Input: 78 -> Output: 15
"""
surya = int(input("Enter a two-digit number: "))

def sum_of_digits(num):
    if 10 <= num <= 99:
        tens = num // 10
        units = num % 10
        return tens + units
    else:
        return "Error: Please enter a two-digit number."

print("Output:", sum_of_digits(surya))