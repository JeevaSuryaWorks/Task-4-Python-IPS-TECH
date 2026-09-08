"""
Question: Get a four-digit number from the user and print its reverse.
Test case:
Input: 7384 -> Output: 4837
"""

surya=int(input("Enter a four-digit number: "))
def reverse_four_digit(num):
    if 1000 <= num <= 9999:
        thousands = num // 1000
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        units = num % 10
        return units * 1000 + tens * 100 + hundreds * 10 + thousands
    else:
        return "Error: Please enter a four-digit number."

print("Output:", reverse_four_digit(surya))