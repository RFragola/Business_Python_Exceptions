# age_verification.py
# Exercise 3: Customer Age Verification for Marketing Campaigns

def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer's age: "))

            if age <= 0:
                print("Age must be a positive number.")
                continue

            return age

        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def main():
    print("=== Customer Age Verification ===")

    try:
        minimum_age = 18

        age = get_customer_age()

        if age >= minimum_age:
            print("Customer is eligible for the promotion.")
        else:
            print("Customer is not eligible for the promotion.")

    except NameError:
        print("Error: A required variable is not defined.")


if __name__ == "__main__":
    main()