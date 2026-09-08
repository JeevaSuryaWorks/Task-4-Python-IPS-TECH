"""
Question: Get a string and a character from the user. Find all positions where the character is present and print them.
Test case:
Input String: hellohellohello
Input Character: h
Output: 1, 6, 11
"""
js = input("Enter a string: ")
ch = input("Enter a character: ")
positions = [i for i in range(len(js)) if js[i] == ch]
print("Output:", ", ".join(map(str, positions)))