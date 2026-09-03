"""
Question: Write a loop program to print the two-digit even numbers whose sum of digits is 6.
Test case:
Output:
24
42
60
"""
print("Output:")
for i in range(10, 100):
    if i % 2 == 0 and (i // 10 + i % 10) == 6:
        print(i)
