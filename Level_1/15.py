"""
Question: Get a four-digit number from the user and only reverse the first two digits of the number, then print the number.
Test case:
Input: 9561 -> Output: 9516
Input: 3859 -> Output: 3895
"""

input=int(input("Enter Number: "))
if(input>=1000 and input<10000):
    js=(input%100)*100+(input//100%10)*10+(input//1000)
    print("Reverse Number:",js)
else:
    print("Please enter a four-digit number.")