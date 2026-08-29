"""
Question: Get a two-digit number from the user and print the one's digit.
Test case:
Input: 45 -> Output: 5
Input: 56 -> Output: 6
"""

s=int(input("Enter Number:"))
if(s>=10 and s<100):
    print(s%10)
else:
    print("Please enter a two-digit number.")


