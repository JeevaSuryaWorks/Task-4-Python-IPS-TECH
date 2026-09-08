"""
Question: Write a program to print the total number of two-digit odd numbers.
Test case:
Output: 45
"""

surya = 0
for i in range(10, 100):
    if i % 2 != 0:
        surya += 1
print("Output:", surya)