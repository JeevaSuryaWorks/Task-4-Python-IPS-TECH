"""
Question: Get a three-digit number from the user and print the digit in the hundred's position.
Test case:
Input: 738 -> Output: 7
"""

surya=int(input("Enter a three-digit number: "))
def hundreds_digit(num):
    if 100 <= num <= 999:
        return num // 100
    else:
        return "Error: Please enter a three-digit number."

print("Output:", hundreds_digit(surya))