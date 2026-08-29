"""
Question: Get a three-digit number from the user and print the one's digit.
Test case:
Input: 456 -> Output: 6
Input: 569 -> Output: 9
"""

s=int(input("Enter Number: "))
if(s>=100 and s<1000):
    js=s%10
    print("One Digit:",js) 
else:
    print("Please enter a three-digit number.")