"""
Question: Get a two-digit number from the user. If the sum of the digits is 10, print 'Success', otherwise print 'Failure'.
Test case:
Input: 56 -> Output: Failure
Input: 37 -> Output: Success
"""

js=int(input("Enter Number: "))
if(js>=10 and js<100):
    if((js//10 + js%10) == 10):
        print("Output: Success")
    else:
        print("Output: Failure")
else:
    print("Please enter a two-digit number.")