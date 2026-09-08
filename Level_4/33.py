"""
Question: Print the total number of non-decreasing numbers from 1000 to 9999. A non-decreasing number has digits that do not decrease from left to right. Example: 1234 is non-decreasing, whereas 2134 is not.
Test case:
Output: 495
"""
js = 0
for i in range(1000, 10000):
    s = str(i)
    if s[0] <= s[1] <= s[2] <= s[3]:
        js += 1
print("Output:", js)