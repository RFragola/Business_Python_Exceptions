# salary_adjustment.py
# Exercise 5: Employee Salary Adjustment Simulator

def get_valid_float(prompt):
    """
    Helper function to safely get a float from the user.
    Keeps prompting until valid numeric input is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=== Employee Salary Adjustment Simulator ===")

    current_salary = get_valid_float("Enter current salary: ")
    adjustment_percentage = get_valid_float("Enter adjustment percentage (0-100): ")

    # Custom validation for percentage range
    if adjustment_percentage < 0:
        print("Adjustment percentage cannot be negative.")
        return
    elif adjustment_percentage > 100:
        print("Adjustment percentage cannot exceed 100%.")
        return

    # Calculate new salary
    new_salary = current_salary * (1 + adjustment_percentage / 100)

    print("\n--- Salary Adjustment Summary ---")
    print(f"Current Salary: ${current_salary:.2f}")
    print(f"Adjustment Percentage: {adjustment_percentage:.2f}%")
    print(f"New Salary: ${new_salary:.2f}")


if __name__ == "__main__":
    main()