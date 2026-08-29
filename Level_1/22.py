"""
Question: Get a number from the user and subtract 5 from it if the number's ten's position digit is odd, then print the result. Do not use 'if'.
Test case:
Input: 685 -> Output: 685
Input: 89172 -> Output: 89167
"""

js=int(input("Enter Number: "))
result = js - ((js // 10) % 2) * 5
print("Output:", result)