"""
Question: Write a function to convert an integer array into a character array and print it.
Test case:
Input: 1 4 5 8 7 6 3 -> Output: 1458763
"""
js = input("Enter the integer array (space-separated): ")
arr = [int(x) for x in js.split()]
char_arr = [str(x) for x in arr]
print("Output:", "".join(char_arr))