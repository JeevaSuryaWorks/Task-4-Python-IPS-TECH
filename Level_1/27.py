"""
Question: Get a three-digit number from the user. If the sum of the digits is 10, print 'Success', otherwise print 'Failure'.
Test case:
Input: 956 -> Output: Failure
Input: 127 -> Output: Success
"""

js=int(input("Enter Number: "))
if(js>=100 and js<1000):
    if((js//100 + js//10%10 + js%10) == 10):
        print("Output: Success")
    else:
        print("Output: Failure")
else:
    print("Please enter a three-digit number.")