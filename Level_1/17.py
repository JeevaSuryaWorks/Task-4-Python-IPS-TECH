"""
Question: Get a two-digit number from the user and make the one's digit 0, then print it.
Test case:
Input: 95 -> Output: 90
Input: 18 -> Output: 10
"""

input=int(input("Enter Number: "))
if(input>=10 and input<100):
    s=(input//10)*10
    print("Output:",s)
else:
    print("Invalid input. Please enter a two-digit number.")