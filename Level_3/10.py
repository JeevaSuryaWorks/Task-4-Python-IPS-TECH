"""
Question: Get a number from the user, find the number of digits, and print it.
Test case:
Input: 34678 -> Output: 5
Input: 12345678 -> Output: 8
"""

num = int(input("Enter a number: "))
def count_digits(num):
    if num == 0:
        return 1
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
print("Output:", count_digits(num))