"""
Question: Write a program to print the biggest 4-digit number which is divisible by 7 and 9.
Test case:
Output: 9954
"""

js = 9999
while js > 0:
    if js % 7 == 0 and js % 9 == 0:
        print(js)
        break
    js -= 1
