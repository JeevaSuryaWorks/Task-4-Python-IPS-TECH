"""
Question: Write a program to get a number from the user and print the reverse of that number.
Test case:
Input: 123456 -> Output: 654321
Input: 76895439 -> Output: 93459867
Input: 675 -> Output: 576
"""
number = int(input("Input: "))
reverse_number = 0
while number > 0:
    reverse_number = reverse_number * 10 + number % 10
    number //= 10
print("Output:", reverse_number)
