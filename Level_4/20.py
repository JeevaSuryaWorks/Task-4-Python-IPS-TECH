"""
Question: Write a program to print the total number of single-digit prime numbers. Assume 0 and 1 are not prime.
Test case:
Output: 4
"""

surya = 0
for i in range(2, 10):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        surya += 1
print("Output:", surya)