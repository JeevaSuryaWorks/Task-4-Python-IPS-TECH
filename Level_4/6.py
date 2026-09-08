"""
Question: Get a two-digit number from the user and print its reverse.
Test case:
Input: 73 -> Output: 37
"""

surya = int(input("Enter a two-digit number: "))
def reverse_two_digit(num):
    if 10 <= num <= 99:
        tens = num // 10
        units = num % 10
        return units * 10 + tens
    else:
        return "Error: Please enter a two-digit number."

print("Output:", reverse_two_digit(surya))