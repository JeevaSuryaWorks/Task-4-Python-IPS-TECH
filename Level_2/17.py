"""
Question: Write a program to get a number from the user, print whether that number is prime, and check whether the sum of its digits is equal to 14.
Test case:
Input: 59 -> Output: Prime & Sum of Digits is 14
Input: 77 -> Output: Not Prime but sum of digits is 14
Input: 13 -> Output: Prime, but sum of Digits is not 14
"""

js=int(input("Enter a number: "))

if js > 1:
    for i in range(2, js):
        if js % i == 0:
            print("Not Prime but sum of digits is", sum(int(digit) for digit in str(js)))
            break
    else:
        if sum(int(digit) for digit in str(js)) == 14:
            print("Prime & Sum of Digits is 14")
        else:
            print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime")