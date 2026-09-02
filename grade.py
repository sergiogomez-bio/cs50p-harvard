"""
CS50P - Lecture 1: Grade Evaluation
Demonstrates comparison operators, chained ranges, and flow optimization.
Author: Sergio Gomez (@sergiogomez-bio)
"""

def main():
    score = int(input("Score: "))

    print("\n--- Evaluation Results ---")
    evaluate_explicit(score)
    evaluate_chained(score)
    evaluate_optimized(score)


def evaluate_explicit(score: int) -> None:
    """Approach 1: Explicit logical AND operators."""
    if score >= 90 and score <= 100:
        print("Approach 1 (AND): Grade: A")
    elif score >= 80 and score < 90:
        print("Approach 1 (AND): Grade: B")
    elif score >= 70 and score < 80:
        print("Approach 1 (AND): Grade: C")
    elif score >= 60 and score < 70:
        print("Approach 1 (AND): Grade: D")
    else:
        print("Approach 1 (AND): Grade: F")


def evaluate_chained(score: int) -> None:
    """Approach 2: Pythonic chained range comparisons (80 <= score < 90)."""
    if 90 <= score <= 100:
        print("Approach 2 (Chained): Grade: A")
    elif 80 <= score < 90:
        print("Approach 2 (Chained): Grade: B")
    elif 70 <= score < 80:
        print("Approach 2 (Chained): Grade: C")
    elif 60 <= score < 70:
        print("Approach 2 (Chained): Grade: D")
    else:
        print("Approach 2 (Chained): Grade: F")


def evaluate_optimized(score: int) -> None:
    """Approach 3: Optimized flow control (questions top-to-bottom)."""
    if score >= 90:
        print("Approach 3 (Optimized): Grade: A")
    elif score >= 80:
        print("Approach 3 (Optimized): Grade: B")
    elif score >= 70:
        print("Approach 3 (Optimized): Grade: C")
    elif score >= 60:
        print("Approach 3 (Optimized): Grade: D")
    else:
        print("Approach 3 (Optimized): Grade: F")


if __name__ == "__main__":
    main()