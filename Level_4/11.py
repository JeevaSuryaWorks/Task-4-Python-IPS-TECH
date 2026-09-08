"""
Question: Get a four-digit number from the user and print the sum of all digits.
Test case:
Input: 7638 -> Output: 24
"""
surya=int(input("Enter a four-digit number: "))

def sum_of_digits(num):
    if 1000 <= num <= 9999:
        thousands = num // 1000
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        units = num % 10
        return thousands + hundreds + tens + units
    else:
        return "Error: Please enter a four-digit number."

print("Output:", sum_of_digits(surya))