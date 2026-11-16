# Personal Expense & Budget Manager

A lightweight, command-line Python application designed to help you track your daily expenses, set a monthly budget, and monitor your spending habits. 

## Features

* **Set a Monthly Budget:** Easily define your spending limit for the month. Your budget is saved locally so it persists between sessions.
* **Add Expenses:** Log individual expenses with a date (YYYY-MM-DD), category, and amount.
* **Category Summary:** View a breakdown of your spending grouped by category.
* **Generate Reports:** Get a comprehensive overview of your total spending, remaining budget, and the percentage of your budget used, along with warnings if you are nearing or exceeding your limit.
* **Persistent Storage:** Expenses are efficiently saved to a CSV file (`expenses.csv`), and your budget is saved to a text file (`budget.txt`).

## Prerequisites

To run this application, you need to have Python installed on your system along with the `pandas` library.

* Python 3.6 or higher
* `pandas` library

## Installation

1. **Clone or Download the Repository:**
   Save the Python script (e.g., `expense_manager.py`) to a local directory on your computer.

2. **Install Dependencies:**
   Open your terminal or command prompt and run the following command to install the required `pandas` library:
   ```bash
   pip install pandas
   ```

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory where you saved the script.
3. Run the script using Python:
   ```bash
   python expense_manager.py
   ```
4. Follow the on-screen menu to interact with the application:
   * Press `1` to set your initial budget.
   * Press `2` to start adding expenses.
   * Press `3` to see where your money is going.
   * Press `4` to generate a full budget report.
   * Press `5` to exit the application.

## Project Structure

When you run the script for the first time, it will automatically generate the necessary data files:

* `expense_manager.py` - The main application script.
* `expenses.csv` - Auto-generated file where your expense records are stored.
* `budget.txt` - Auto-generated file that securely stores your current budget.