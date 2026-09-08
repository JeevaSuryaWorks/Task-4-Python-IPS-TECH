"""
Question: Write a program to print the sum of single-digit prime numbers.
Test case:
Output: 18
"""

js=0
for i in range(2, 10):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        js += i
print("Output:", js)