"""
Question: Write a program to get a 4-digit number from the user and print whether the middle two digits form a prime number.
Test case:
Input: 6359 -> Output: Not Prime
Input: 3517 -> Output: Prime
"""

js=int(input("Enter a 4-digit number: "))
if 1000 <= js <= 9999:
    middle_two_digits = (js // 10) % 100

    if middle_two_digits > 1:
        for i in range(2, middle_two_digits):
            if middle_two_digits % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")
else:
    print("Please enter a valid 4-digit number.")