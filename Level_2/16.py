"""
Question: Write a program to get a number from the user and print whether that number is prime or not.
Test case:
Input: 31 -> Output: Prime
Input: 27 -> Output: Not Prime
"""

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")