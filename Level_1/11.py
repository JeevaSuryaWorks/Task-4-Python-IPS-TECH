"""
Question: Get a two-digit number from the user and print the sum of the digits.
Test case:
Input: 56 -> Output: 11
Input: 69 -> Output: 15
"""

js=int(input("Enter Number: "))
if(js>=10 and js<100):
    s=(js//10)+(js%10)
    print("Total Sum:",s)
else:
    print("Please enter a two-digit number.")