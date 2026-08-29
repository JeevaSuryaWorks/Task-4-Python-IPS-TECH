"""
Question: Get a three-digit number from the user and print the ten's digit.
Test case:
Input: 456 -> Output: 5
Input: 569 -> Output: 6
"""

s=int(input("Enter Number: "))
if(s>=100 and s<1000):
    js=(s//10)%10
    print("Ten's Digit:",js) 
else:
    print("Please enter a three-digit number.")