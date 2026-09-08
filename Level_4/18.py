"""
Question: Write a program to print the sum of all two-digit odd numbers.
Test case:
Output: 2475
"""

surya = 0
for i in range(10, 100):    
    if i % 2 != 0:
        surya += i
print("Output:", surya)