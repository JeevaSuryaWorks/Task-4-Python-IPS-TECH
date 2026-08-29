"""
Question: Get a four-digit number from the user and subtract 5 from it if the ten's digit position and hundred's digit position are the same, then print the result. Do not use 'if'.
Test case:
Input: 7595 -> Output: 7595
Input: 3772 -> Output: 3767
"""

js=int(input("Enter Number: "))
result = js - ((js // 10) % 10 == (js // 100) % 10) * 5
print("Output:", result)