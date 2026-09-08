"""
Question: Write a program to get a number from the user and print the total number of single-digit perfect square numbers in the number.
Test case:
Input: 123456789 -> Output: 3
Input: 987531 -> Output: 2
"""
js = int(input("Enter a number: "))
perfect_squares = {1, 4, 9}
count = 0
for digit in str(js):
    if int(digit) in perfect_squares:
        count += 1
print("Output:", count)
