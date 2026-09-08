"""
Question: Write a program to print the total count of numbers less than 100000 whose sum of digits is 14.
Test case:
Output: 4995
"""

js = 0
for i in range(100000):
    if sum(int(digit) for digit in str(i)) == 14:
        js += 1
print("Output:", js)