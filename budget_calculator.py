def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Please enter a number that is 0 or greater.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Student Budget Calculator")
    print("-------------------------")

    income = get_amount("Enter your monthly income: $")
    rent = get_amount("Enter your monthly rent: $")
    food = get_amount("Enter your monthly food expenses: $")
    other = get_amount("Enter your other monthly expenses: $")

    total_expenses = rent + food + other
    remaining_balance = income - total_expenses
    suggested_savings = max(remaining_balance * 0.20, 0)

    print("\nBudget Summary")
    print("--------------")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Remaining balance: ${remaining_balance:.2f}")
    print(f"Suggested savings transfer: ${suggested_savings:.2f}")


if __name__ == "__main__":
    main()
