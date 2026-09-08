"""
Question: Get a number from the user and subtract 5 from that number and print the result. Write your code inside the function.
Test case:
Input: 45 -> Output: 40
Input: 56789 -> Output: 56784
"""

js=int(input("Enter a number: "))
def subtract_five(num):
    return num - 5

print("Output:", subtract_five(js))