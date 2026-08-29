"""
Question: Get two 2-digit numbers from the user and print the sum of the digits of the bigger number.
Test case:
Input: 56, 78 -> Output: 15
Input: 14, 65 -> Output: 11
"""

js=int(input("Enter First Number: "))
js1=int(input("Enter Second Number: "))
if(js>=10 and js<100 and js1>=10 and js1<100):
    if(js > js1):
        print("Output:", (js // 10) + (js % 10))
    else:
        print("Output:", (js1 // 10) + (js1 % 10))
else:
    print("Output: Failure")