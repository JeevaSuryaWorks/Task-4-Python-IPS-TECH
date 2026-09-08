"""
Question: Get a number string up to 50 digits and convert it into an integer array.
Test case:
Input: 12345 -> Output: [1, 2, 3, 4, 5]
"""
js = input("Enter a number string up to 50 digits: ")
def convert_to_integer_array(s):
    return [int(digit) for digit in s]

