"""
Question: Get two numbers of up to 50 digits, perform addition, and print the result.
Test case:
Input: 123456789123456789, 987654321987654321
Output: 1111111111111111110
"""
js1 = input("Enter the first number (up to 50 digits): ")
js2 = input("Enter the second number (up to 50 digits): ")

num1 = int(js1)
num2 = int(js2)
result = num1 + num2
print("Output:", result)