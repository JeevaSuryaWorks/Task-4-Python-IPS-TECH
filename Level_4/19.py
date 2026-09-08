"""
Question: Write a program to print the sum of all three-digit odd numbers.
Test case:
Output: 247500
"""

surya = 0
for i in range(99, 1000):    
    if i % 2 != 0:
        surya += i
print("Output:", surya)