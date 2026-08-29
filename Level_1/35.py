"""
Question: Get two 3-digit numbers from the user. Add the one's and hundred's digits of both numbers. Print the sum of all the digits of the number whose sum of one's and hundred's digits is bigger.
Test case:
Input: 856, 978 -> Output: 24
Input: 128, 365 -> Output: 11
"""

js=int(input("Enter First Number: "))
js1=int(input("Enter Second Number: "))
if(js>=100 and js<1000 and js1>=100 and js1<1000):
    sum_of_digits_1 = (js // 100) + (js % 10)
    sum_of_digits_2 = (js1 // 100) + (js1 % 10)
    if(sum_of_digits_1 > sum_of_digits_2):
        total_sum = (js // 100) + (js // 10 % 10) + (js % 10)
        print("Output:", total_sum)
    elif(sum_of_digits_2 > sum_of_digits_1):
        total_sum = (js1 // 100) + (js1 // 10 % 10) + (js1 % 10)
        print("Output:", total_sum)
    else:
        print("Output: Failure")