"""
Question: Get a three-digit number from the user and print the reverse of the number.
Test case:
Input: 561 -> Output: 165
Input: 859 -> Output: 958
"""

input=int(input("Enter Number: "))
if(input>=100 and input<1000):
    js=(input%10)*100+(input//10%10)*10+(input//100)
    print("Reverse Number:",js)
else:
    print("Please enter a three-digit number.")