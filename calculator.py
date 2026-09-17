"""
Simple Interest Calculator
---------------------------
Formula:
    Simple Interest (SI) = (Principal * Rate * Time) / 100
    Total Amount (A)     = Principal + SI

This program takes Principal amount, Rate of interest (per year),
and Time (in years) from the user and calculates the Simple Interest
and the Total Amount.
"""


def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """Calculate simple interest given principal, rate and time."""
    simple_interest = (principal * rate * time) / 100
    return simple_interest


def main():
    print("=== Simple Interest Calculator ===")

    try:
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (per year, %): "))
        time = float(input("Enter Time (in years): "))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return

    if principal < 0 or rate < 0 or time < 0:
        print("Values cannot be negative.")
        return

    simple_interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + simple_interest

    print("\n--- Result ---")
    print(f"Principal Amount : {principal}")
    print(f"Rate of Interest : {rate}%")
    print(f"Time Period      : {time} year(s)")
    print(f"Simple Interest  : {simple_interest:.2f}")
    print(f"Total Amount     : {total_amount:.2f}")


if __name__ == "__main__":
    main()