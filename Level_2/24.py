"""
Question: Write a program to get a number from the user and print the total number of two-digit perfect square numbers in the number.
Test case:
Input: 163496481 -> Output: 4
Input: 364925 -> Output: 4
"""

js = int(input("Enter a number: "))
perfect_squares = {16, 25, 36, 49, 64, 81}
count = 0
for i in range(len(str(js)) - 1):
    two_digit_number = int(str(js)[i:i+2])
    if two_digit_number in perfect_squares:
        count += 1
print("Output:", count) 