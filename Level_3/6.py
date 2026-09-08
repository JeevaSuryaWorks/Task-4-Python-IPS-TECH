"""
Question: Get a number from the user and reverse that number.
Test case:
Input: 123 -> Output: 321
Input: 56789 -> Output: 98765
"""

js = int(input("Enter a number: "))
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
print("Output:", reverse_number(js))