"""
Question: Write a program to get a number from the user. If the first digit is even, print the same number. If the first digit is odd, subtract 1 from the first digit and print the number.
Test case:
Input: 123456 -> Output: 023456
Input: 96895439 -> Output: 86895439
Input: 675 -> Output: 675
Input: 575 -> Output: 475
"""
number = int(input("Input: "))
number_str = str(number)
if len(number_str) > 0:
    if int(number_str[0]) % 2 == 0:
        print("Output:", number_str)
    else:
        print("Output:", str(int(number_str[0]) - 1) + number_str[1:])
else:
    print("Output:", number_str)