"""
Question: Get an integer and print each digit as a character, one character per line.
Test case:
Input: 12345
Output:
1
2
3
4
5
"""

js = int(input("Enter an integer: "))
def print_digits(num):
    for digit in str(num):
        print(digit)

print_digits(js)