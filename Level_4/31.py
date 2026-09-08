"""
Question: Print the number of zeroes encountered between 0 and 1000.
Test case:
Output: 193
(This counts zeroes from 1 through 1000.)
"""
surya = 0
for i in range(1, 1001):
    surya += str(i).count('0')
print("Output:", surya)
