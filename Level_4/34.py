"""
Question: Print the total number of palindrome numbers less than 100000. Examples: 101, 12321, 656, 99899.
Test case:
Output: 1098
"""
js = 0
for i in range(1, 100000):
    if str(i) == str(i)[::-1]:
        js += 1
print("Output:", js)