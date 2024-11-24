# Assignment: Create a Simple ATM System in Python
# Objective:
# To develop a basic ATM system using Python that allows users to perform essential banking operations such as checking balance, 
# depositing money, and withdrawing money.

# Requirements:
# User Authentication:
# Implement a simple login system where users can log in with a predefined account number and PIN.
# Use a hardcoded account number and PIN for this assignment (e.g., Account Number: 123456, PIN: 1234).

# Main Menu:
# After successful login, display a menu with the following options:
# Check Balance
# Deposit Money
# Withdraw Money
# Exit

# Functions:
# Create functions for each operation:
# check_balance(balance): Displays the current balance.
# deposit(balance, amount): Increases the balance by the deposit amount.
# withdraw(balance, amount): Decreases the balance by the withdrawal amount if sufficient funds are available.

# Data Validation:
# Ensure that the deposit and withdrawal amounts are positive numbers.
# When withdrawing, ensure that the user has sufficient funds.

# Loop Until Exit:
# Allow the user to perform operations until they choose to exit the program.

# Error Handling:
# Handle invalid input gracefully (e.g., non-numeric values for amounts).

# Implementation Steps:
# Start by defining a main function that will handle the user interaction.
# Create a loop for the main menu that keeps running until the user chooses to exit.
# Implement the functions required for each banking operation.
# Ensure to maintain and update the user’s balance throughout the session.
#--------------------------------------------------------------------------------------------------------------------

# Predefined account information
account_number = "123456"
pin = "1234"

# Initial balance
balance = 1000.00  # Starting balance for the user

# Function to check balance
def check_balance(balance):
    print(f"\nYour current balance is: € {balance:.2f}")

# Function to deposit money
def deposit(balance, amount):
    if amount > 0:
        balance += amount      # i.e. balance = balance + amount
        print(f"\nSuccessfully deposited € {amount:.2f}. New balance: € {balance:.2f}")
    else:
        print("\nDeposit amount must be positive.")
    return balance

# Function to withdraw money
def withdraw(balance, amount):
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"\nSuccessfully withdrew € {amount:.2f}. New balance: € {balance:.2f}")
        else:
            print("\nInsufficient funds.")
    else:
        print("\nWithdrawal amount must be positive.")
    return balance

# Function for user authentication
def authenticate():
    user_account = input("\nEnter your account number: ")
    user_pin = input("Enter your PIN: ")
    if user_account == account_number and user_pin == pin:
        print("\nLogin successful!")
        return True
    else:
        print("\nInvalid account number or PIN. Please try again.")
        return False

# Main ATM system function
def atm_system():
    # Authenticate user
    if not authenticate():
        return

# ATM main menu loop
    global balance  # Access the global balance
    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            try:
                amount = float(input("\nEnter amount to deposit: "))
                balance = deposit(balance, amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid amount.")
        
        elif choice == "3":
            try:
                amount = float(input("\nEnter amount to withdraw: "))
                balance = withdraw(balance, amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid amount.")
        
        elif choice == "4":
            print("\nThank you for using the ATM. Goodbye!")
            break
        
        else:
            print("\nInvalid option. Please choose between 1 and 4.")

# Run the ATM system
atm_system()