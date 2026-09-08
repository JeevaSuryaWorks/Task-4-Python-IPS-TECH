"""
Question: Write a program to get a number from the user and print the total number of two-digit odd numbers in the number.
Test case:
Input: 12345678 -> Output: 3
Input: 987531 -> Output: 4
"""

js=int(input("Enter a number: "))
count = 0
for i in range(len(str(js)) - 1):
    two_digit_number = int(str(js)[i:i+2])
    if 10 <= two_digit_number <= 99 and two_digit_number % 2 != 0:
        count += 1
print("Output:", count)