"""
CS50P - Lecture 1: Conditionals and Logical Operators.
Practice script comparing integers using different logical approaches.
Author: Sergio Gomez (@sergiogomez-bio)
"""

def main():
    # Prompt user for integer inputs
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    print("\n--- Evaluation Results ---")
    compare_detailed(x, y)
    compare_inequality(x, y)
    compare_equality(x, y)


def compare_detailed(x, y):
    """Approach 1: Chained conditionals for three distinct outcomes."""
    if x < y:
        print("Approach 1: x is less than y")
    elif x > y:
        print("Approach 1: x is greater than y")
    else:
        print("Approach 1: x is equal to y")


def compare_inequality(x, y):
    """Approach 2: Logical OR comparison for inequality."""
    if x < y or x > y:
        print("Approach 2: x is not equal to y")
    else:
        print("Approach 2: x is equal to y")


def compare_equality(x, y):
    """Approach 3: Direct equality check."""
    if x == y:
        print("Approach 3: x is equal to y")
    else:
        print("Approach 3: x is not equal to y")


if __name__ == "__main__":
    main()