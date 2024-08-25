#import tkinter as tk: Imports the tkinter library for creating graphical user interfaces (GUIs). The tkinter library is aliased as tk for easier reference.
#from tkinter import messagebox: Imports the messagebox module from tkinter, which provides a way to display message boxes (like alerts or errors).
#import matplotlib.pyplot as plt: Imports the pyplot module from the matplotlib library, which is used for creating static, animated, and interactive visualizations in Python (in this case, a pie chart).

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class FinancialTracker: #class FinancialTracker: Defines a new class called FinancialTracker. A class is a blueprint for creating objects (in this case, a financial tracker).
    def __init__(self, root): #def __init__(self, root): The __init__ method is a special method that initializes objects created from the class. root is the main window of the tkinter application passed as an argument.
        self.root = root
        self.root.title("Financial Tracker")
        
        self.total_income = 0
        self.total_expenses = 0
        self.expenses = {}
        self.savings_goal = 0

        # Income input
        tk.Label(root, text="Income:").grid(row=0, column=0)
        self.income_entry = tk.Entry(root)
        self.income_entry.grid(row=0, column=1)
        tk.Button(root, text="Add Income", command=self.add_income).grid(row=0, column=2)

        # Expense input
        tk.Label(root, text="Expense Name:").grid(row=1, column=0)
        self.expense_name_entry = tk.Entry(root)
        self.expense_name_entry.grid(row=1, column=1)

        tk.Label(root, text="Expense Amount:").grid(row=2, column=0)
        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.grid(row=2, column=1)
        
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=2, column=2)

        # Savings Goal
        tk.Label(root, text="Savings Goal:").grid(row=3, column=0)
        self.savings_goal_entry = tk.Entry(root)
        self.savings_goal_entry.grid(row=3, column=1)
        tk.Button(root, text="Set Savings Goal", command=self.set_savings_goal).grid(row=3, column=2)

        # Buttons to display data
        tk.Button(root, text="Show Summary", command=self.show_summary).grid(row=4, column=0, columnspan=3)
        tk.Button(root, text="Show Spending Breakdown", command=self.show_spending_breakdown).grid(row=5, column=0, columnspan=3)
        
        # Result display
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=6, column=0, columnspan=3)

    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.total_income += income
            self.income_entry.delete(0, tk.END)
            self.update_summary()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for income.")

    def add_expense(self):
        try:
            name = self.expense_name_entry.get()
            amount = float(self.expense_amount_entry.get())
            if name in self.expenses:
                self.expenses[name] += amount
            else:
                self.expenses[name] = amount
            self.total_expenses += amount
            self.expense_name_entry.delete(0, tk.END)
            self.expense_amount_entry.delete(0, tk.END)
            self.update_summary()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for expense amount.")

    def set_savings_goal(self):
        try:
            self.savings_goal = float(self.savings_goal_entry.get())
            self.savings_goal_entry.delete(0, tk.END)
            self.update_summary()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for savings goal.")

    def update_summary(self):
        remaining_income = self.total_income - self.total_expenses
        if self.savings_goal > 0:
            savings_percentage = (remaining_income / self.savings_goal) * 100
            savings_message = f"Savings Goal: ${self.savings_goal} ({savings_percentage:.2f}% achieved)"
        else:
            savings_message = "Savings Goal: Not set"

        self.result_label.config(
            text=f"Total Income: ${self.total_income}\n"
                 f"Total Expenses: ${self.total_expenses}\n"
                 f"Remaining Income: ${remaining_income}\n"
                 f"{savings_message}"
        )

    def show_summary(self):
        self.update_summary()

    def show_spending_breakdown(self):
        if not self.expenses:
            messagebox.showinfo("No Expenses", "No expenses to display.")
            return
        
        labels = self.expenses.keys()
        sizes = self.expenses.values()

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Spending Breakdown')
        plt.show()

# Main application
root = tk.Tk()
app = FinancialTracker(root)
root.mainloop()
