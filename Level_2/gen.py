"""
generate_level2_files.py

Run this INSIDE your "Level 2" folder to auto-create all 30 problem files,
each pre-filled with a docstring containing the Question and Test case.

Usage:
    python generate_level2_files.py

By default it will NOT overwrite files that already exist. Pass --force to
overwrite everything.
"""

import os
import sys

# Each value is (question, list_of_testcase_lines)
problems = {
    1: (
        "Write a loop program to print 1 to 5 one by one.",
        ["Output:", "1", "2", "3", "4", "5"],
    ),
    2: (
        "Write a loop program to print 5 to 1 one by one.",
        ["Output:", "5", "4", "3", "2", "1"],
    ),
    3: (
        "Write a loop program to print the sum of 1 to 5.",
        ["Output: 15"],
    ),
    4: (
        "Write a loop program to print the sum of 6 to 1.",
        ["Output: 21"],
    ),
    5: (
        "Write a loop program to print odd numbers from 1 to 9.",
        ["Output:", "1", "3", "5", "7", "9"],
    ),
    6: (
        "Write a loop program to print the two-digit odd numbers below 20.",
        ["Output:", "11", "13", "15", "17", "19"],
    ),
    7: (
        "Write a loop program to print the two-digit odd numbers whose sum of digits is 7.",
        ["Output:", "25", "43", "61"],
    ),
    8: (
        "Write a loop program to print the two-digit even numbers whose sum of digits is 6.",
        ["Output:", "24", "42", "60"],
    ),
    9: (
        "Write a loop program to print the sum of two-digit numbers whose one's digit is 5.",
        ["Output: 495"],
    ),
    10: (
        "Write a loop program to print the sum of two-digit odd numbers whose ten's digit is 7.",
        ["Output: 375"],
    ),
    11: (
        "Write a program to get a number from the user and print the total number of digits in that number.",
        ["Input: 123456 -> Output: 6", "Input: 76895439 -> Output: 8", "Input: 675 -> Output: 3"],
    ),
    12: (
        "Write a program to get a number from the user and print the sum of all digits.",
        ["Input: 123456 -> Output: 21", "Input: 76895439 -> Output: 51", "Input: 675 -> Output: 18"],
    ),
    13: (
        "Write a program to get a number from the user and print the reverse of that number.",
        ["Input: 123456 -> Output: 654321", "Input: 76895439 -> Output: 93459867", "Input: 675 -> Output: 576"],
    ),
    14: (
        "Write a program to get a number from the user and interchange the first and last digits, then print the result.",
        ["Input: 123456 -> Output: 623451", "Input: 76895439 -> Output: 96895437", "Input: 675 -> Output: 576"],
    ),
    15: (
        "Write a program to get a number from the user. If the first digit is even, print the same "
        "number. If the first digit is odd, subtract 1 from the first digit and print the number.",
        [
            "Input: 123456 -> Output: 023456",
            "Input: 96895439 -> Output: 86895439",
            "Input: 675 -> Output: 675",
            "Input: 575 -> Output: 475",
        ],
    ),
    16: (
        "Write a program to get a number from the user and print whether that number is prime or not.",
        ["Input: 31 -> Output: Prime", "Input: 27 -> Output: Not Prime"],
    ),
    17: (
        "Write a program to get a number from the user, print whether that number is prime, and "
        "check whether the sum of its digits is equal to 14.",
        [
            "Input: 59 -> Output: Prime & Sum of Digits is 14",
            "Input: 77 -> Output: Not Prime but sum of digits is 14",
            "Input: 13 -> Output: Prime, but sum of Digits is not 14",
        ],
    ),
    18: (
        "Write a program to get a number from the user and print whether the last two digits form a prime number.",
        ["Input: 359 -> Output: Prime", "Input: 3577 -> Output: Not Prime"],
    ),
    19: (
        "Write a program to get a 4-digit number from the user and print whether the middle two digits form a prime number.",
        ["Input: 6359 -> Output: Not Prime", "Input: 3517 -> Output: Prime"],
    ),
    20: (
        "Write a program to print the total number of single-digit prime numbers.",
        ["Output: 4"],
    ),
    21: (
        "Write a program to get a number from the user and print the total number of digits that are odd.",
        ["Input: 12345678 -> Output: 4", "Input: 987531 -> Output: 5"],
    ),
    22: (
        "Write a program to get a number from the user and print the total number of two-digit odd numbers in the number.",
        ["Input: 12345678 -> Output: 3", "Input: 987531 -> Output: 4"],
    ),
    23: (
        "Write a program to get a number from the user and print the total number of single-digit perfect square numbers in the number.",
        ["Input: 123456789 -> Output: 3", "Input: 987531 -> Output: 2"],
    ),
    24: (
        "Write a program to get a number from the user and print the total number of two-digit perfect square numbers in the number.",
        ["Input: 163496481 -> Output: 4", "Input: 364925 -> Output: 4"],
    ),
    25: (
        "Write a program to get a number from the user and print the total number of single-digit prime numbers in the number.",
        ["Input: 163496481 -> Output: 1", "Input: 364925 -> Output: 3"],
    ),
    26: (
        "Write a program to print the biggest 4-digit number which is divisible by 7 and 9.",
        ["Output: 9954"],
    ),
    27: (
        "Write a program to print the total count of numbers less than 100000 whose sum of digits is 14.",
        ["Output: 4995"],
    ),
    28: (
        "Write a program to get two numbers from the user and print the LCM of those numbers.",
        ["Input: 12, 18 -> Output: 36", "Input: 15, 20 -> Output: 60"],
    ),
    29: (
        "Write a program to get three numbers from the user and print the LCM of those numbers.",
        ["Input: 2, 3, 4 -> Output: 12", "Input: 4, 6, 8 -> Output: 24"],
    ),
    30: (
        "Write a program to get two numbers from the user and print the HCF of those numbers.",
        ["Input: 12, 18 -> Output: 6", "Input: 24, 36 -> Output: 12"],
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
        print("    python generate_level2_files.py --force")


if __name__ == "__main__":
    main()