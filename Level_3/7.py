"""
Question: Get two numbers from the user and compare them. If they are the same, print 'Same'; otherwise print 'Not Same'.
Test case:
Input: 123, 123 -> Output: Same
Input: 56789, 12345 -> Output: Not Same
"""

input=input("Enter two numbers separated by a comma: ")
num1, num2 = map(int, input.split(','))

if num1 == num2:
    print("Same")
else:
    print("Not Same")