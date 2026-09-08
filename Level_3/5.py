"""
Question: Get a number from the user and count the number of zeros in that number.
Test case:
Input: 100 -> Output: 2
Input: 1060030 -> Output: 4
"""

js = int(input("Enter a number: "))
def count_zeros(num):
    count = 0
    while num > 0:
        if num % 10 == 0:
            count += 1
        num //= 10
    return count
print("Output:", count_zeros(js))