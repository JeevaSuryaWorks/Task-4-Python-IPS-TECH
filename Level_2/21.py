"""
Question: Write a program to get a number from the user and print the total number of digits that are odd.
Test case:
Input: 12345678 -> Output: 4
Input: 987531 -> Output: 5
"""

js = int(input("Enter a number: "))
odd_count = sum(1 for digit in str(js) if int(digit) % 2 != 0)
print("Output:", odd_count)