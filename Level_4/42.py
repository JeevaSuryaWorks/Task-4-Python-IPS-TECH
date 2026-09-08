"""
Question: Get a string and find its length.
Test case:
Input: Hello -> Output: 5
Input: Python Programming -> Output: 18
"""

js=input("Enter a string: ")
def string_length(s):
    return len(s)
print("Output:", string_length(js))