"""
Question: Get a two-digit number from the user and print the ten's digit.
Test case:
Input: 45 -> Output: 4
Input: 56 -> Output: 5
"""

j=int(input("Enter Number:"))
if(j >= 10 and j < 100):
    print(j//10)
else:
    print("Please enter a two-digit number.")
