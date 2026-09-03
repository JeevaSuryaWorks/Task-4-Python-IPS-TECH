"""
Question: Write a program to get a number from the user and print the total number of digits in that number.
Test case:
Input: 123456 -> Output: 6
Input: 76895439 -> Output: 8
Input: 675 -> Output: 3
"""
number = int(input("Input: "))
count = 0
while number > 0:
    count += 1
    number //= 10
print("Output:", count)
