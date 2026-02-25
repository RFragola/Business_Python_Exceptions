# financial_ratio.py
# Exercise 4: Financial Ratio Calculator with Defensive Programming

def main():
    print("=== Profit Margin Ratio Calculator ===")

    while True:  # Infinite loop until valid inputs are provided
        try:
            profit = float(input("Enter profit amount: "))
            revenue = float(input("Enter revenue amount: "))

            ratio = profit / revenue  # May raise ZeroDivisionError

        except ValueError:
            # Silent reprompt for invalid float input
            pass

        except ZeroDivisionError:
            # Silent reprompt if revenue is zero
            pass

        else:
            # Runs only if no exceptions occur
            percentage = ratio * 100
            print(f"\nProfit Margin Ratio: {percentage:.2f}%")
            break  # Exit loop after successful calculation


if __name__ == "__main__":
    main()