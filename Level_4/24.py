"""
Question: Write a program to print the sum of all two-digit prime numbers.
Test case:
Output: 1043
"""
surya = 0
for i in range(10, 100):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        surya += i
print("Output:", surya)