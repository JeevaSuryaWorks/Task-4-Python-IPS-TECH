"""
Question: Get a three-digit number from the user and make the ten's digit 0, then print it.
Test case:
Input: 695 -> Output: 605
Input: 182 -> Output: 102
"""

js=int(input("Enter Number: "))
if(js>=100 and js<1000):
    s=(js//100)*100+(js%10)
    print("Output:",s)
else:
    print("Please enter a three-digit number.")