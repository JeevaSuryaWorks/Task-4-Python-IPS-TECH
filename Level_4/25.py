"""
Question: Write a program to print the sum of all three-digit prime numbers.
Test case:
Output: 75067
"""
surya = 0
for i in range(100, 1000):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        surya += i
print("Output:", surya)