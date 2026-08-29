"""
Question: Get a three-digit number from the user. If the sum of the one's digit and hundred's digit is less than 10, print 'Success', otherwise print 'Failure'.
Test case:
Input: 569 -> Output: Failure
Input: 316 -> Output: Success
"""

js=int(input("Enter Number: "))
if(js>=100 and js<1000):
    if((js//100 + js%10) < 10):
        print("Output: Success")
    else:
        print("Output: Failure")
else:
    print("Please enter a three-digit number.")