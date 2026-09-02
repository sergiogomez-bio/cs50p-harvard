"""
CS50P - Lecture 1: Structural Pattern Matching
Demonstrates the match/case statement, string normalization, and OR (|) patterns.
Author: Sergio Gomez (@sergiogomez-bio)
"""

def main():
    # Prompt user and sanitize input (strip whitespace, capitalize first letters)
    name = input("What's your name? ").strip().title()

    print("\n--- Evaluation Results ---")
    evaluate_if_chain(name)
    evaluate_match_pattern(name)


def evaluate_if_chain(name: str) -> None:
    """Approach 1: Traditional if / elif / else chain."""
    if name == "Harry" or name == "Hermione" or name == "Ron":
        print("Approach 1 (if/elif): Gryffindor")
    elif name == "Draco":
        print("Approach 1 (if/elif): Slytherin")
    else:
        print("Approach 1 (if/elif): Who?")


def evaluate_match_pattern(name: str) -> None:
    """Approach 2: Python 3.10+ match statement with combined cases (|)."""
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Approach 2 (match): Gryffindor")
        case "Draco":
            print("Approach 2 (match): Slytherin")
        case _:
            print("Approach 2 (match): Who?")


if __name__ == "__main__":
    main()



