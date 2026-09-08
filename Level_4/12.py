"""
Question: Get a number from the user and print its reverse.
Test case:
Input: 123456 -> Output: 654321
"""
surya = int(input("Enter a number: "))

def reverse_number(num):
    if num < 0:
        return "Error: Please enter a positive number."
    else:
        return int(str(num)[::-1])

print("Output:", reverse_number(surya))
