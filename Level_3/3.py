"""
Question: Get a number from the user and check whether the sum of digits is 14, then print the result.
Test case:
Input: 59 -> Output: Sum of Digits is 14
Input: 123 -> Output: Sum of Digits is not 14
"""

js=int(input("Enter a number: "))
if sum(int(digit) for digit in str(js)) == 14:
    print("Output: Sum of Digits is 14")
else:
    print("Output: Sum of Digits is not 14")