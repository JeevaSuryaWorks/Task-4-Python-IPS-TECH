"""
Question: Get two 2-digit numbers from the user. If the sum of the numbers is less than 100, print the sum; otherwise print the difference.
Test case:
Input: 56, 78 -> Output: 22
Input: 14, 65 -> Output: 79
"""

js=int(input("Enter First Number: "))
js1=int(input("Enter Second Number: "))
if(js>=10 and js<100 and js1>=10 and js1<100):
    if((js + js1) < 100):
        print("Output:", (js + js1))
    else:
        print("Output:", abs(js - js1))
else:
    print("Difference:", js+js1-100)
