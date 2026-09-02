"""
CS50P - Lecture 1: Parity Checker & Boolean Abstraction
Demonstrates modulo operator (%), helper functions, ternary syntax, and boolean returns.
Author: Sergio Gomez (@sergiogomez-bio)
"""

def main():
    x = int(input("What's x? "))

    # Evaluate using the idiomatic boolean function
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even_verbose(n: int) -> bool:
    """Approach 1: Explicit if/else conditional check."""
    if n % 2 == 0:
        return True
    else:
        return False


def is_even_ternary(n: int) -> bool:
    """Approach 2: Conditional expression (ternary operator)."""
    return True if n % 2 == 0 else False


def is_even(n: int) -> bool:
    """Approach 3: Direct boolean expression return (Idiomatic Python)."""
    return n % 2 == 0


if __name__ == "__main__":
    main()