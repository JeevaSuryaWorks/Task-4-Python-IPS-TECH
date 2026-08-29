"""
Question: Get a three-digit number from the user and print the sum of the digits.
Test case:
Input: 562 -> Output: 13
Input: 469 -> Output: 19
"""

ips=int(input("Enter Number: "))
if(ips>=100 and ips<1000):
    js=(ips//100)+(ips//10%10)+(ips%10)
    print("Total Sum:",js)
else:
    print("Please enter a three-digit number.")