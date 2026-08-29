"""
Question: Get a three-digit number from the user. If the sum of the digits is less than 10, print the sum; otherwise repeatedly add the digits of the sum until the result is a single digit.
Test case:
Input: 123 -> Output: 6
Input: 149 -> Output: 5
Input: 991 -> Output: 1
"""

js=int(input("Enter Number: "))
if(js>=100 and js<1000):
    sum_of_digits = (js // 100) + (js // 10 % 10) + (js % 10)
    while sum_of_digits >= 10:
        sum_of_digits = (sum_of_digits // 10) + (sum_of_digits % 10)
    print("Output:", sum_of_digits)
else:
    print("Output: Failure")