"""
Question: Write a program to get a number from the user and print the sum of all digits.
Test case:
Input: 123456 -> Output: 21
Input: 76895439 -> Output: 51
Input: 675 -> Output: 18
"""
number = int(input("Input: "))
total_sum = 0
while number > 0:
    total_sum += number % 10
    number //= 10
print("Output:", total_sum)