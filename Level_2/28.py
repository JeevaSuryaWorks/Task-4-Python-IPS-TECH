"""
Question: Write a program to get two numbers from the user and print the LCM of those numbers.
Test case:
Input: 12, 18 -> Output: 36
Input: 15, 20 -> Output: 60
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

s1 = int(input("Enter first number: "))
s2 = int(input("Enter second number: "))
print("Output:", lcm(s1, s2))