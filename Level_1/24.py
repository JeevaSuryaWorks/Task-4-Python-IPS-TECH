"""
Question: Get a three-digit number from the user and subtract 5 from it if the one's digit and hundred's digit are the same, then print the result. Do not use 'if'.
Test case:
Input: 595 -> Output: 590
Input: 372 -> Output: 372
"""

js=int(input("Enter Number: "))
result = js - ((js // 100) == (js % 10)) * 5
print("Output:", result)