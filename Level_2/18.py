"""
Question: Write a program to get a number from the user and print whether the last two digits form a prime number.
Test case:
Input: 359 -> Output: Prime
Input: 3577 -> Output: Not Prime
"""

js=int(input("Enter a number: "))
last_two_digits = js % 100

if last_two_digits > 1:
    for i in range(2, last_two_digits):
        if last_two_digits % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")