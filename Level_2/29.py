"""
Question: Write a program to get three numbers from the user and print the LCM of those numbers.
Test case:
Input: 2, 3, 4 -> Output: 12
Input: 4, 6, 8 -> Output: 24
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

s1 = int(input("Enter first number: "))
s2 = int(input("Enter second number: "))
s3 = int(input("Enter third number: "))

result = lcm(lcm(s1, s2), s3)
print("Output:", result)