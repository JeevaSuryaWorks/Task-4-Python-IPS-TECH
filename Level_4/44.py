"""
Question: Get a string of numbers up to 50 digits and remove all leading zeroes.
Test case:
Input: 00000012345 -> Output: 12345
"""

js=input("Enter a string of numbers: ")
def remove_leading_zeroes(s):
    return s.lstrip('0') or '0'

print("Output:", remove_leading_zeroes(js))