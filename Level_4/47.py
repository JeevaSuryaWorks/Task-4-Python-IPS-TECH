"""
Question: Add two integer arrays of up to 50 digits and store the result in a 51-digit array.
Test case:
Input: [1, 2, 3], [4, 5, 6]
Output: [5, 7, 9]
"""

js1 = input("Enter the first integer array (comma-separated): ")
js2 = input("Enter the second integer array (comma-separated): ")

arr1 = [int(x) for x in js1.split(',')]
arr2 = [int(x) for x in js2.split(',')]
result = [a + b for a, b in zip(arr1, arr2)]
print("Output:", result)