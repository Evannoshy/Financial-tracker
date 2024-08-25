#imports tkinter library which creates graphical user interfaces (GUI), and name it tk for easy reference
import tkinter as tk

#imports messagebox module from tkinter which allows us to dispaly message boxes
from tkinter import messagebox 

#imports pyplot module from matplotlib which allows us to create graphs 
import matplotlib.pyplot as plt

#defines a new class which is a blueprint for creating the financial tracker
class FinancialTracker:

#intializes objects created from above class. root is the main window of the tkinter application passed as an argument
#_init_ is used when the object is first created. It initializes the skills variable to an empty list initially.
    def __init__(self, root): #The interpreter isn't initialized until you create the root window

        self.root = root #stores the root window in the variable 'self root' for use in other methods
        self.root.title("Financial Tracker") #root window serves as the main window of the GUI
        
        #sets variables to start at 0 
        self.total_income = 0
        self.total_expenses = 0
        self.expenses = {}
        self.savings_goal = 0

        # Income input 
        tk.Label(root, text="Income:").grid(row=0, column=0) #creates a label with text income and places it at (0,0)
        self.income_entry = tk.Entry(root) #creates a textbox where user can input their income 
        self.income_entry.grid(row=0, column=1) #places text box at (1,0)
        tk.Button(root, text="Add Income", command=self.add_income).grid(row=0, column=2) #creates a button labeled 'add income' that calls the self.add_income when clicked

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
        
        # Creates a label to display results and places label in the grid
        # Result display
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=6, column=0, columnspan=3)
        #Retrieve income entered by the user and converts it to a floating point number
    def add_income(self):
        try:
            income = float(self.income_entry.get()) 
            self.total_income += income
            self.income_entry.delete(0, tk.END) #clears income entry field after adding the income
            self.update_summary() #refreshes the display
        except ValueError: #similar to calculator, prevents user from inputting non numerical values
            messagebox.showerror("Input Error", "Please enter a valid number for income.")

    def add_expense(self):
        try:
            name = self.expense_name_entry.get()
            amount = float(self.expense_amount_entry.get())
            if name in self.expenses: #Checks if the expense name already exists in the expenses dictionary.
                self.expenses[name] += amount #If it exists, adds the new amount to the existing amount.
            else:
                self.expenses[name] = amount #If it doesn't exist, adds a new entry to the dictionary
            self.total_expenses += amount
            self.expense_name_entry.delete(0, tk.END) #clear input fields
            self.expense_amount_entry.delete(0, tk.END)
            self.update_summary()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for expense amount.")

    def set_savings_goal(self): #same concept as expense, refer to above
        try:
            self.savings_goal = float(self.savings_goal_entry.get())
            self.savings_goal_entry.delete(0, tk.END)
            self.update_summary()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for savings goal.")

    def update_summary(self): #same concept as expense, refer to above
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
        #plotting pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Spending Breakdown')
        plt.show()

# Main application
root = tk.Tk()
app = FinancialTracker(root)
root.mainloop()
