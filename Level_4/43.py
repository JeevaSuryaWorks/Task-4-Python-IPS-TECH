"""
Question: Get a string and check whether it is a valid number.
Test case:
Input: 1234567 -> Output: Valid Number
Input: 12abc35 -> Output: Not a Valid Number
"""

js = input("Enter a string: ")
def is_valid_number(s):
    return s.isdigit()

print("Output:", "Valid Number" if is_valid_number(js) else "Not a Valid Number")