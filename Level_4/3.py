"""
Question: Get a three-digit number from the user and print the digit in the one's position.
Test case:
Input: 738 -> Output: 8
"""

js=int(input("Enter a three-digit number: "))
def ones_digit(num):
    if 100 <= num <= 999:
        return num % 10
    else:
        return "Error: Please enter a three-digit number."

print("Output:", ones_digit(js))