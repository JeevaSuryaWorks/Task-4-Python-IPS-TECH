"""
Question: Get a two-digit number from the user and make the ten's digit 1, then print it.
Test case:
Input: 95 -> Output: 15
Input: 82 -> Output: 12
"""

js=int(input("Enter Number: "))
if(js>=10 and js<100):
    s=10+(js%10)
    print("Output:",s)
else:
    print("Invalid input.")