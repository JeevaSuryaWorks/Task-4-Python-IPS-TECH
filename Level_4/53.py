"""
Question: Get a string and count all the words in it.
Test case:
Input: Welcome to HCL Tech -> Output: 4
"""
js = input("Enter a string: ")
words = js.split()
print("Output:", len(words))