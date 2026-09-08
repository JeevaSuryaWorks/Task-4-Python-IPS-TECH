"""
Question: Write a program to get a number from the user and print the total number of single-digit prime numbers in the number.
Test case:
Input: 163496481 -> Output: 1
Input: 364925 -> Output: 3
"""

js = int(input("Enter a number: "))
single_digit_primes = {2, 3, 5, 7}
count = 0
for digit in str(js):
    if int(digit) in single_digit_primes:
        count += 1
print("Output:", count)