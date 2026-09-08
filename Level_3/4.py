"""
Question: Get a number from the user and check whether it is prime or not, then print the result.
Test case:
Input: 61 -> Output: Number is Prime
Input: 1200 -> Output: Number is not Prime
"""

js=int(input("Enter a number: "))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if is_prime(js):
    print("Output: Number is Prime")
else:
    print("Output: Number is not Prime")