"""
Question: Get a two-digit number from the user and subtract 5 from it if the sum of the digits is odd, then print the result. Do not use 'if'.
Test case:
Input: 95 -> Output: 95
Input: 72 -> Output: 67
"""

js=int(input("Enter Number: "))
result = js - ((js // 10 + js % 10) % 2) * 5
print("Output:", result)