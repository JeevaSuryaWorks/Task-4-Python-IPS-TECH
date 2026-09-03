"""
Question: Write a loop program to print the sum of two-digit odd numbers whose ten's digit is 7.
Test case:
Output: 375
"""
total_sum = 0
for i in range(70, 80):
    if i % 2 != 0:
        total_sum += i
print("Output:", total_sum)

