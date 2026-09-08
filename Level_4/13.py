"""
Question: Get a number from the user and print the sum of all digits.
Test case:
Input: 123456 -> Output: 21
"""

surya = int(input("Enter a number: "))
def sum_of_digits(num):
    if num < 0:
        return "Error: Please enter a positive number."
    else:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total

print("Output:", sum_of_digits(surya))