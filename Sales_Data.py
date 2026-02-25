# sales_data.py
# Exercise 1: Handling Invalid Sales Data Input

def get_valid_number(prompt, data_type):
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("=== Retail Sales Data Entry ===")

    # Get validated inputs
    units_sold = get_valid_number("Enter number of units sold (integer): ", int)
    price_per_unit = get_valid_number("Enter price per unit (float): ", float)

    # Calculate total revenue
    total_revenue = units_sold * price_per_unit

    # Display results
    print("\n--- Sales Summary ---")
    print(f"Units Sold: {units_sold}")
    print(f"Price per Unit: ${price_per_unit:.2f}")
    print(f"Total Revenue: ${total_revenue:.2f}")


if __name__ == "__main__":
    main()