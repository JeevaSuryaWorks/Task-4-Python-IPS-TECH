"""
Question: Write a loop program to print the two-digit odd numbers whose sum of digits is 7.
Test case:
Output:
25
43
61
"""
print("Output:")
for i in range(10, 100):
    if i % 2 != 0 and (i // 10 + i % 10) == 7:
        print(i)