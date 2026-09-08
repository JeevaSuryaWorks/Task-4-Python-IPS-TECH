"""
Question: Get a three-digit number from the user and print the digit in the ten's position.
Test case:
Input: 738 -> Output: 3
"""

jeeva=int(input("Enter a three-digit number: "))
def tens_digit(num):
    if 100 <= num <= 999:
        return (num // 10) % 10
    else:
        return "Error: Please enter a three-digit number."
print("Output:", tens_digit(jeeva))