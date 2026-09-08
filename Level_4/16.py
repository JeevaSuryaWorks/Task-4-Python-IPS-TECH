"""
Question: Write a program to print the total number of three-digit odd numbers.
Test case:
Output: 450
"""

surya = 0
for i in range(100, 1000):
    if i % 2 != 0:
        surya += 1
print("Output:", surya)