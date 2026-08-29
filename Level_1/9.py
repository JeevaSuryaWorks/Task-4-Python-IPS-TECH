"""
Question: Get a three-digit number from the user and print the hundred's digit.
Test case:
Input: 456 -> Output: 4
Input: 569 -> Output: 5
"""

s=int(input("Enter Number: "))
if(s>=100 and s<1000):
    js=s//100
    print("Hundred Digit:",js) 
else:
    print("Please enter a three-digit number.")