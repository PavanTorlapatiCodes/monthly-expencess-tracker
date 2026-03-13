import pandas as pd
import os
from datetime import datetime

# CSV file for data storage
csv_file = 'expenses.csv'

# Create CSV if it doesn't exist
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Category'])
    df.to_csv(csv_file, index=False)
    print("New expenses file created!")


def add_expense():
    date = input("Enter date (YYYY-MM-DD, or Enter for today): ") or datetime.now().strftime('%Y-%m-%d')
    desc = input("Description: ")
    amount = float(input("Amount (₹): "))
    category = input("Category (Food/Transport/Shopping/Other): ")

    new_row = pd.DataFrame({
        'Date': [date],
        'Description': [desc],
        'Amount': [amount],
        'Category': [category]
    })

    df = pd.read_csv(csv_file)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(csv_file, index=False)
    print(f"✅ Added: {desc} - ₹{amount} ({category})")


def view_expenses():
    df = pd.read_csv(csv_file)
    if df.empty:
        print("No expenses yet. Add some!")
    else:
        print("\n📊 All Expenses:")
        print(df)
        total = df['Amount'].sum()
        print(f"\n💰 Total spent: ₹{total:.2f}")


def view_by_category():
    df = pd.read_csv(csv_file)
    if not df.empty:
        print("\n📈 Spending by Category:")
        summary = df.groupby('Category')['Amount'].sum()
        print(summary)
        print(f"\n💎 Grand total: ₹{summary.sum():.2f}")


def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Quit")

        choice = input("Choose (1-4): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            print("Thanks! Check expenses.csv for data.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
