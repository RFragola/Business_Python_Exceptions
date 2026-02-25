def main():
    print("=== Inventory Management System ===")

    while True:  # Infinite loop until valid inputs are entered
        try:
            inventory = int(input("Enter current inventory level: "))
            threshold = int(input("Enter minimum reorder threshold: "))

            # Calculate percentage of inventory compared to threshold
            percentage = (inventory / threshold) * 100

            print(f"\nInventory is at {percentage:.2f}% of the reorder threshold.")

            # Check if reorder is needed
            if inventory < threshold:
                print("Reorder Alert: Inventory is below the minimum threshold!")
            else:
                print("Inventory level is sufficient.")

            break  # Exit loop if everything works correctly

        except ValueError:
            print("Invalid input. Please enter whole numbers only.\n")

        except ZeroDivisionError:
            print("Threshold cannot be zero. Please enter a valid threshold.\n")


if __name__ == "__main__":
    main()