"""
Question: Get a two-digit number from the user and print the reverse of the number.
Test case:
Input: 56 -> Output: 65
Input: 59 -> Output: 95
"""

tech=int(input("Enter Number: "))
if(tech>=10 and tech<100):
    js=(tech%10)*10+(tech//10)
    print("Reverse Number:",js)
else:
    print("Please enter a two-digit number.")