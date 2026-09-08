"""
Question: Get a character and print its ASCII value.
Test case:
Input: A -> Output: 65
Input: a -> Output: 97
"""
char = input("Enter a character: ")
def ascii_value(c):
    return ord(c)
print("Output:", ascii_value(char))