"""
generate_level4_files.py

Run this INSIDE your "Level 4" folder to auto-create all 53 problem files,
each pre-filled with a docstring containing the Question and Test case.

Note: A few problems in the Level 4 PDF (31-34, 40-42) didn't list a final
expected output directly under "Testcase" - those are marked "[Added]" below,
matching values worked out from the question itself.

Usage:
    python generate_level4_files.py

By default it will NOT overwrite files that already exist. Pass --force to
overwrite everything.
"""

import os
import sys

# Each value is (question, list_of_testcase_lines)
problems = {
    1: (
        "Get a two-digit number from the user and print the digit in the one's position.",
        ["Input: 78 -> Output: 8"],
    ),
    2: (
        "Get a two-digit number from the user and print the digit in the ten's position.",
        ["Input: 78 -> Output: 7"],
    ),
    3: (
        "Get a three-digit number from the user and print the digit in the one's position.",
        ["Input: 738 -> Output: 8"],
    ),
    4: (
        "Get a three-digit number from the user and print the digit in the ten's position.",
        ["Input: 738 -> Output: 3"],
    ),
    5: (
        "Get a three-digit number from the user and print the digit in the hundred's position.",
        ["Input: 738 -> Output: 7"],
    ),
    6: (
        "Get a two-digit number from the user and print its reverse.",
        ["Input: 73 -> Output: 37"],
    ),
    7: (
        "Get a three-digit number from the user and print its reverse.",
        ["Input: 738 -> Output: 837"],
    ),
    8: (
        "Get a four-digit number from the user and print its reverse.",
        ["Input: 7384 -> Output: 4837"],
    ),
    9: (
        "Get a two-digit number from the user and print the sum of all digits.",
        ["Input: 78 -> Output: 15"],
    ),
    10: (
        "Get a three-digit number from the user and print the sum of all digits.",
        ["Input: 738 -> Output: 18"],
    ),
    11: (
        "Get a four-digit number from the user and print the sum of all digits.",
        ["Input: 7638 -> Output: 24"],
    ),
    12: (
        "Get a number from the user and print its reverse.",
        ["Input: 123456 -> Output: 654321"],
    ),
    13: (
        "Get a number from the user and print the sum of all digits.",
        ["Input: 123456 -> Output: 21"],
    ),
    14: (
        "Write a program to print the total number of single-digit odd numbers.",
        ["Output: 5"],
    ),
    15: (
        "Write a program to print the total number of two-digit odd numbers.",
        ["Output: 45"],
    ),
    16: (
        "Write a program to print the total number of three-digit odd numbers.",
        ["Output: 450"],
    ),
    17: (
        "Write a program to print the sum of all single-digit odd numbers.",
        ["Output: 25"],
    ),
    18: (
        "Write a program to print the sum of all two-digit odd numbers.",
        ["Output: 2475"],
    ),
    19: (
        "Write a program to print the sum of all three-digit odd numbers.",
        ["Output: 247500"],
    ),
    20: (
        "Write a program to print the total number of single-digit prime numbers. "
        "Assume 0 and 1 are not prime.",
        ["Output: 4"],
    ),
    21: (
        "Write a program to print the total number of two-digit prime numbers.",
        ["Output: 21"],
    ),
    22: (
        "Write a program to print the total number of three-digit prime numbers.",
        ["Output: 143"],
    ),
    23: (
        "Write a program to print the sum of single-digit prime numbers.",
        ["Output: 18"],
    ),
    24: (
        "Write a program to print the sum of all two-digit prime numbers.",
        ["Output: 1043"],
    ),
    25: (
        "Write a program to print the sum of all three-digit prime numbers.",
        ["Output: 75067"],
    ),
    26: (
        "Print the smallest three-digit prime number.",
        ["Output: 101"],
    ),
    27: (
        "Print the largest three-digit prime number.",
        ["Output: 997"],
    ),
    28: (
        "Print the smallest four-digit prime number.",
        ["Output: 1009"],
    ),
    29: (
        "Print the largest four-digit prime number.",
        ["Output: 9973"],
    ),
    30: (
        "Print the largest eight-digit prime number.",
        ["Output: 99999989"],
    ),
    31: (
        "Print the number of zeroes encountered between 0 and 1000.",
        ["Output: 193", "(This counts zeroes from 1 through 1000.)"],
    ),
    32: (
        "Print the total number of prime numbers below 1,000,000 whose sum of digits "
        "is equal to 14. Example: 59 -> 5 + 9 = 14",
        ["Output: 1218"],
    ),
    33: (
        "Print the total number of non-decreasing numbers from 1000 to 9999. A "
        "non-decreasing number has digits that do not decrease from left to right. "
        "Example: 1234 is non-decreasing, whereas 2134 is not.",
        ["Output: 495"],
    ),
    34: (
        "Print the total number of palindrome numbers less than 100000. "
        "Examples: 101, 12321, 656, 99899.",
        ["Output: 1098"],
    ),
    35: (
        "Get two numbers from the user and find their LCM.",
        ["Input: 20, 30 -> Output: 60"],
    ),
    36: (
        "Get a character and print its ASCII value.",
        ["Input: A -> Output: 65", "Input: a -> Output: 97"],
    ),
    37: (
        "Get an ASCII number and print its corresponding character.",
        ["Input: 65 -> Output: A", "Input: 97 -> Output: a"],
    ),
    38: (
        "Get a string and print the same string.",
        ["Input: Hello World -> Output: Hello World"],
    ),
    39: (
        "Get a number as a string and print its integer value.",
        ['Input: "12345" -> Output: 12345'],
    ),
    40: (
        "Get an integer and print it as a string.",
        ['Input: 12345 -> Output: "12345"'],
    ),
    41: (
        "Get an integer and print each digit as a character, one character per line.",
        ["Input: 12345", "Output:", "1", "2", "3", "4", "5"],
    ),
    42: (
        "Get a string and find its length.",
        ["Input: Hello -> Output: 5", "Input: Python Programming -> Output: 18"],
    ),
    43: (
        "Get a string and check whether it is a valid number.",
        ["Input: 1234567 -> Output: Valid Number", "Input: 12abc35 -> Output: Not a Valid Number"],
    ),
    44: (
        "Get a string of numbers up to 50 digits and remove all leading zeroes.",
        ["Input: 00000012345 -> Output: 12345"],
    ),
    45: (
        "Get a number up to 50 digits and reverse it.",
        ["Input: 12345678912345 -> Output: 54321987654321"],
    ),
    46: (
        "Get a number string up to 50 digits and convert it into an integer array.",
        ["Input: 12345 -> Output: [1, 2, 3, 4, 5]"],
    ),
    47: (
        "Add two integer arrays of up to 50 digits and store the result in a 51-digit array.",
        ["Input: [1, 2, 3], [4, 5, 6]", "Output: [5, 7, 9]"],
    ),
    48: (
        "Adjust the carry in an integer array. Convert a two-digit number into a single "
        "digit and add the carry to the previous position.",
        ["Input: 6 12 3 15 7", "Output: 7 2 4 5 7"],
    ),
    49: (
        "Write a function to convert an integer array into a character array and print it.",
        ["Input: 1 4 5 8 7 6 3 -> Output: 1458763"],
    ),
    50: (
        "Get two numbers of up to 50 digits, perform addition, and print the result.",
        [
            "Input: 123456789123456789, 987654321987654321",
            "Output: 1111111111111111110",
        ],
    ),
    51: (
        "Get a string and a character from the user. Find all positions where the "
        "character is present and print them.",
        ["Input String: hellohellohello", "Input Character: h", "Output: 1, 6, 11"],
    ),
    52: (
        "Get a main string and a substring. Check whether the substring is present in "
        "the main string and print its position.",
        ["Input String: hellosurabee", "Input Substring: sura", "Output: 6"],
    ),
    53: (
        "Get a string and count all the words in it.",
        ["Input: Welcome to HCL Tech -> Output: 4"],
    ),
}


def build_docstring(question: str, testcase_lines: list) -> str:
    lines = ['"""', f"Question: {question}", "Test case:"]
    lines.extend(testcase_lines)
    lines.append('"""')
    lines.append("")
    lines.append("")
    return "\n".join(lines)


def main():
    force = "--force" in sys.argv
    created, skipped = [], []

    for num, (question, testcase_lines) in problems.items():
        filename = f"{num}.py"
        if os.path.exists(filename) and not force:
            skipped.append(filename)
            continue
        with open(filename, "w", encoding="utf-8") as f:
            f.write(build_docstring(question, testcase_lines))
        created.append(filename)

    print(f"Created: {len(created)} file(s) -> {', '.join(created) if created else 'none'}")
    print(f"Skipped (already existed): {len(skipped)} file(s) -> {', '.join(skipped) if skipped else 'none'}")
    if skipped:
        print("\nTip: run with --force to overwrite existing files too:")
        print("    python generate_level4_files.py --force")


if __name__ == "__main__":
    main()