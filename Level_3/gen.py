"""
generate_level3_files.py

Run this INSIDE your "Level 3" folder to auto-create all 10 problem files,
each pre-filled with a docstring containing the Question and Test case.

Note: Level 3 problems ask you to write your code inside a function.

Usage:
    python generate_level3_files.py

By default it will NOT overwrite files that already exist. Pass --force to
overwrite everything.
"""

import os
import sys

# Each value is (question, list_of_testcase_lines)
problems = {
    1: (
        "Get a number from the user and add 2 to that number and print the result. "
        "Write your code inside the function.",
        ["Input: 45 -> Output: 47", "Input: 56789 -> Output: 56791"],
    ),
    2: (
        "Get a number from the user and subtract 5 from that number and print the result. "
        "Write your code inside the function.",
        ["Input: 45 -> Output: 40", "Input: 56789 -> Output: 56784"],
    ),
    3: (
        "Get a number from the user and check whether the sum of digits is 14, then print the result.",
        ["Input: 59 -> Output: Sum of Digits is 14", "Input: 123 -> Output: Sum of Digits is not 14"],
    ),
    4: (
        "Get a number from the user and check whether it is prime or not, then print the result.",
        ["Input: 61 -> Output: Number is Prime", "Input: 1200 -> Output: Number is not Prime"],
    ),
    5: (
        "Get a number from the user and count the number of zeros in that number.",
        ["Input: 100 -> Output: 2", "Input: 1060030 -> Output: 4"],
    ),
    6: (
        "Get a number from the user and reverse that number.",
        ["Input: 123 -> Output: 321", "Input: 56789 -> Output: 98765"],
    ),
    7: (
        "Get two numbers from the user and compare them. If they are the same, print "
        "'Same'; otherwise print 'Not Same'.",
        ["Input: 123, 123 -> Output: Same", "Input: 56789, 12345 -> Output: Not Same"],
    ),
    8: (
        "Get a number from the user and check whether its digits are in ascending order.",
        ["Input: 1234 -> Output: Yes", "Input: 5687 -> Output: No"],
    ),
    9: (
        "Get a two-digit number from the user and swap the digits.",
        ["Input: 34 -> Output: 43", "Input: 56 -> Output: 65"],
    ),
    10: (
        "Get a number from the user, find the number of digits, and print it.",
        ["Input: 34678 -> Output: 5", "Input: 12345678 -> Output: 8"],
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
        print("    python generate_level3_files.py --force")


if __name__ == "__main__":
    main()