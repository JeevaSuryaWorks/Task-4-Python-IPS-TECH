"""
Question: Get a three-digit number from the user and make the one's digit 2, then print it.
Test case:
Input: 695 -> Output: 692
Input: 182 -> Output: 182
"""

js=int(input("Enter Number: "))
if(js>=100 and js<1000):
    s=(js//10)*10+2
    print("Output:",s)
else:
    print("Please enter a three-digit number.")