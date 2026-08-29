"""
Question: Get two 3-digit numbers from the user. Print the difference between the one's digit and hundred's digit of the number whose ten's digit is bigger than the other number's ten's digit.
Test case:
Input: 856, 978 -> Output: 1
Input: 128, 365 -> Output: 2
"""

js=int(input("Enter First Number: "))
js1=int(input("Enter Second Number: "))
if(js>=100 and js<1000 and js1>=100 and js1<1000):
    tens_digit_1 = js // 10 % 10
    tens_digit_2 = js1 // 10 % 10
    if(tens_digit_1 > tens_digit_2):
        difference = abs((js % 10) - (js // 100))
        print("Output:", difference)
    elif(tens_digit_2 > tens_digit_1):
        difference = abs((js1 % 10) - (js1 // 100))
        print("Output:", difference)
    else:
        print("Output: Failure")