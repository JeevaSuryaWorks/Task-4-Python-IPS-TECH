"""
Question: Get a two-digit number from the user and swap the digits.
Test case:
Input: 34 -> Output: 43
Input: 56 -> Output: 65
"""

input_num = int(input("Enter a two-digit number: "))
def swap_digits(num):
    if 10 <= num <= 99:
        tens = num // 10
        units = num % 10
        swapped_num = units * 10 + tens
        return swapped_num
    else:
        return "Error: Please enter a two-digit number."
print("Output:", swap_digits(input_num))