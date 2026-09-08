"""
Question: Get a number from the user and check whether its digits are in ascending order.
Test case:
Input: 1234 -> Output: Yes
Input: 5687 -> Output: No
"""

input_num = int(input("Enter a number: "))
def is_ascending(num):
    prev_digit = 10  # Initialize to a digit greater than any single digit
    while num > 0:
        current_digit = num % 10
        if current_digit >= prev_digit:
            return False
        prev_digit = current_digit
        num //= 10
    return True
print("Output:", "Yes" if is_ascending(input_num) else "No")