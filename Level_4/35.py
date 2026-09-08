"""
Question: Get two numbers from the user and find their LCM.
Test case:
Input: 20, 30 -> Output: 60
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

js = input("Enter two numbers separated by a comma: ")
num1, num2 = map(int, js.split(','))
print("Output:", lcm(num1, num2))