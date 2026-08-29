"""
Question: Get a four-digit number from the user. If the sum of the ten's digit and hundred's digit equals 10, and one of the digits is more than 7, print 'Success', otherwise print 'Failure'.
Test case:
Input: 4649 -> Output: Failure
Input: 9286 -> Output: Success
"""

js=int(input("Enter Number: "))
if(js>=1000 and js<10000):
    tens_digit = js // 10 % 10
    hundreds_digit = js // 100 % 10
    if((tens_digit + hundreds_digit) == 10 and (tens_digit > 7 or hundreds_digit > 7)):
        print("Output: Success")
    else:
        print("Output: Failure")
else:
    print("Output: Failure")