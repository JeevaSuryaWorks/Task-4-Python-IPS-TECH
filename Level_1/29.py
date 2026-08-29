"""
Question: Get a four-digit number from the user. If the sum of the ten's digit and hundred's digit is greater than 10, print 'Success', otherwise print 'Failure'.
Test case:
Input: 7529 -> Output: Failure
Input: 9386 -> Output: Success
"""

js=int(input("Enter Number: "))
if(js>=1000 and js<10000):
    if((js//100%10 + js//10%10) > 10):
        print("Output: Success")
    else:
        print("Output: Failure")
else:
    print("Please enter a four-digit number.")