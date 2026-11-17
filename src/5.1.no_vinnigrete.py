"""Draw a random date and report whether it falls on a Monday."""

from datetime import date, timedelta
from random import randint


def no_vinnigrete(first_date, second_date):
    """Draw uniformly from the dates between two ISO dates, inclusive."""
    start, end = sorted((date.fromisoformat(first_date), date.fromisoformat(second_date)))
    return start + timedelta(days=randint(0, (end - start).days))


def main():
    """Read two dates and print the draw and any Monday message."""
    first_date = input("First date (YYYY-MM-DD): ").strip()
    second_date = input("Second date (YYYY-MM-DD): ").strip()
    selected_date = no_vinnigrete(first_date, second_date)
    print(selected_date.isoformat())
    if selected_date.weekday() == 0:
        print("אין לי ויניגרט!")


if __name__ == "__main__":
    main()
