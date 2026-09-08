"""
Question: Print the largest three-digit prime number.
Test case:
Output: 997
"""
surya = 999
while True:
    is_prime = True
    for j in range(2, int(surya**0.5) + 1):
        if surya % j == 0:
            is_prime = False
            break
    if is_prime:
        print("Output:", surya)
        break
    surya -= 1