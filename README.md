Exercise 1: Handling Invalid Sales Data Input
- Prompts user to enter the number of units sold (integer) and price per unit (float), using a reusable get_valid_number function with try-except to handle ValueError and reprompt until valid input is provided
- Returns the total revenue (units × price) after validating inputs

Exercise 2: Inventory Quantity Checker with Error Handling
- Prompts user to enter current inventory level and minimum reorder threshold (integers), using try-except inside a loop to handle invalid inputs and prevent crashes
- Returns a reorder alert if inventory is below threshold and safely handles ValueError and ZeroDivisionError when calculating percentage levels

Exercise 3: Customer Age Verification for Marketing Campaigns
- Prompts user to enter customer age (integer) using a get_customer_age function that loops until a valid positive integer is entered, handling ValueError and demonstrating NameError handling
- Returns eligibility status for age-restricted promotions (18+ required)

Exercise 4: Financial Ratio Calculator with Defensive Programming
- Prompts user to enter profit and revenue (floats) in an infinite loop, using try-except-else to handle ValueError and ZeroDivisionError, and pass for silent reprompting
- Returns the calculated profit margin percentage when valid inputs are provided

Exercise 5: Employee Salary Adjustment Simulator
- Prompts user to enter current salary (float) and adjustment percentage (float between 0–100), using helper functions and try-except for input validation
- Returns the new adjusted salary, including validation against invalid or negative percentage values