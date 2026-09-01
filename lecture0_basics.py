"""
CS50P - Lecture 0: Functions, Variables, and String/Numeric Methods.
Practice script by Sergio Gomez (@sergiogomez-bio).
"""

def main():
    # Execute string manipulation practice
    format_user_name()
    
    # Execute numeric formatting practice
    calculate_and_format_numbers()


def format_user_name():
    """Demonstrates string cleaning, splitting, and f-string formatting."""
    # Prompts for name, removes leading/trailing whitespace, and capitalizes each word
    raw_name = input("What's your name? ")
    cleaned_name = raw_name.strip().title()

    # Splits the name into first and last name (if provided)
    if " " in cleaned_name:
        first_name, last_name = cleaned_name.split(" ", 1)
        print(f"Hello, {first_name}! Full name registered as: {cleaned_name}")
    else:
        print(f"Hello, {cleaned_name}!")


def calculate_and_format_numbers():
    """Demonstrates float conversion, rounding, and standard number formatting."""
    # Floating-point inputs and operations
    x = float(input("Enter first decimal number (x): "))
    y = float(input("Enter second decimal number (y): "))

    # Addition and rounding
    total = round(x + y)

    # Output using international comma separator format (e.g., 1,000)
    print(f"Formatted total sum: {total:,}")


if __name__ == "__main__":
    main()
