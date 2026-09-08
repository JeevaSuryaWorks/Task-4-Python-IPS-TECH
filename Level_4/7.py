"""
Question: Get a three-digit number from the user and print its reverse.
Test case:
Input: 738 -> Output: 837
"""

surya=int(input("Enter a three-digit number: "))
def reverse_three_digit(num):
    if 100 <= num <= 999:
        hundreds = num // 100
        tens = (num // 10) % 10
        units = num % 10
        return units * 100 + tens * 10 + hundreds
    else:
        return "Error: Please enter a three-digit number."

print("Output:", reverse_three_digit(surya))