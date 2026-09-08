"""
Question: Get a main string and a substring. Check whether the substring is present in the main string and print its position.
Test case:
Input String: hellosurabee
Input Substring: sura
Output: 6
"""
js = input("Enter the main string: ")
sub = input("Enter the substring: ")
if sub in js:
    print("Output:", js.index(sub))
else:
    print("Output: -1")