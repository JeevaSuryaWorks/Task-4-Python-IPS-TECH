"""
Question: Get a two-digit number from the user and print the digit in the ten's position.
Test case:
Input: 78 -> Output: 7
"""

num=int(input("Enter a two-digit number: "))
def tens_digit(num):
    if 10 <= num <= 99:
        return num // 10
    else:
        return "Error: Please enter a two-digit number."
print("Output:", tens_digit(num))