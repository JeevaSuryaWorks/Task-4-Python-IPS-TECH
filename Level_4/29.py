"""
Question: Print the largest four-digit prime number.
Test case:
Output: 9973
"""
surya = 9999
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