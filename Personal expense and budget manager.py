from datetime import datetime
import os
import pandas as pd

FILE = "expenses.csv"

if not os.path.exists(FILE):
  df = pd.DataFrame(columns=["Date", "Category", "Amount"])
  df.to_csv(FILE, index=False)


def read_expenses():
  return pd.read_csv(FILE)


def set_budget():
  global budget

  try:
    amount = float(input("Enter your monthly budget: "))

    if amount <= 0:
      print("Invalid budget. Enter a positive amount.")
      return

    budget = amount
    print(f"Monthly budget set: {budget:g}")

  except ValueError:
    print("Invalid input. Enter a number.")


def add_expense():
  date = input("Enter date (YYYY-MM-DD): ")
  category = input("Enter category: ")

  try:
    datetime.strptime(date, "%Y-%m-%d")

  except ValueError:
    print("Invalid date. Use YYYY-MM-DD.")
    return

  if not category.strip():
    print("Invalid category.")
    return

  try:
    amount = float(input("Enter amount: "))

    if amount <= 0:
      print("Invalid amount. Amount must be positive.")
      print("Expense not saved.")
      return

  except ValueError:
    print("Invalid amount. Enter a number.")
    return

  df = read_expenses()

  new_expense = pd.DataFrame(
      [{"Date": date, "Category": category.strip(), "Amount": amount}]
  )

  df = pd.concat([df, new_expense], ignore_index=True)

  df.to_csv(FILE, index=False)

  print("Expense saved.")


def category_summary():
  df = read_expenses()

  if df.empty:
    print("No expenses found.")
    return

  summary = df.groupby("Category")["Amount"].sum()

  print("\nCategory-wise Spending:")

  for category, amount in summary.items():
    print(f"{category}: {amount:g}")


def generate_report():
  df = read_expenses()

  if budget is None:
    print("Please set your budget first.")
    return

  total_spent = df["Amount"].sum()
  remaining = budget - total_spent
  percentage = (total_spent / budget) * 100

  print("\n----- Budget Report -----")

  if not df.empty:
    summary = df.groupby("Category")["Amount"].sum()

    for category, amount in summary.items():
      print(f"{category}: {amount:g}")

  # Matching the exact Test Case 4 format with a pipe separator
  print(f"\nTotal spent: {total_spent:g} | Remaining: {remaining:g}")

  if percentage > 100:
    print(f"Budget exceeded! {percentage:.2f}% used.")

  elif percentage == 100:
    print(f"Budget fully used ({percentage:.2f}%).")

  elif percentage >= 80:
    print(f"Warning: {percentage:.2f}% of the budget used.")

  else:
    print(f"{percentage:.2f}% of the budget used.")


budget = None

while True:
  print("\n===== PERSONAL EXPENSE & BUDGET MANAGER =====")

  print("1. Set Budget")
  print("2. Add Expense")
  print("3. Category Summary")
  print("4. Generate Report")
  print("5. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    set_budget()

  elif choice == "2":
    add_expense()

  elif choice == "3":
    category_summary()

  elif choice == "4":
    generate_report()

  elif choice == "5":
    print("Thank you for using Expense Manager!")
    break

  else:
    print("Invalid choice. Please select 1 to 5.")