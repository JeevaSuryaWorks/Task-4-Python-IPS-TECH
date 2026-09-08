"""
Question: Write a program to print the total number of single-digit prime numbers.
Test case:
Output: 4
"""

js = 0
for i in range(1, 10):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            js += 1
print(js)