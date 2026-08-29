"""
Question: Get a four-digit number from the user and only reverse the last two digits of the number, then print the number.
Test case:
Input: 9561 -> Output: 5961
Input: 3859 -> Output: 8359
"""

js=int(input("Enter Number: "))
if(js>=1000 and js<10000):
    s=(js//1000)*1000+(js//100%10)*100+(js%10)*10+(js//10%10)
    print("Reverse Number:",s)