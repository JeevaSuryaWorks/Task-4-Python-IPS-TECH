"""
Question: Print the total number of prime numbers below 1,000,000 whose sum of digits is equal to 14. Example: 59 -> 5 + 9 = 14
Test case:
Output: 1218
"""

js=0
for i in range(2, 1000000):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime and sum(int(digit) for digit in str(i)) == 14:
        js += 1
print("Output:", js)