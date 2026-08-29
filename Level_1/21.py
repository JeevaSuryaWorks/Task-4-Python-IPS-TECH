"""
Question: Get a number from the user and subtract 5 from it if the number is odd, then print the result. Do not use 'if'.
Test case:
Input: 695 -> Output: 690
Input: 182 -> Output: 182
"""

input=int(input("Enter Number: "))
result = input - (input % 2) * 5
print("Output:", result)