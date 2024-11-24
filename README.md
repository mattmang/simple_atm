Assignment: Create a Simple ATM System in Python

Objective:
To develop a basic ATM system using Python that allows users to perform essential banking operations such as checking balance, depositing money, and withdrawing money.

Requirements:
User Authentication:
Implement a simple login system where users can log in with a predefined account number and PIN.
Use a hardcoded account number and PIN for this assignment (e.g., Account Number: 123456, PIN: 1234).
Main Menu:

After successful login, display a menu with the following options:
Check Balance
Deposit Money
Withdraw Money
Exit

Functions:
Create functions for each operation:
check_balance(balance): Displays the current balance.
deposit(balance, amount): Increases the balance by the deposit amount.
withdraw(balance, amount): Decreases the balance by the withdrawal amount if sufficient funds are available.

Data Validation:
Ensure that the deposit and withdrawal amounts are positive numbers.
When withdrawing, ensure that the user has sufficient funds.
Loop Until Exit:

Allow the user to perform operations until they choose to exit the program.

Error Handling:
Handle invalid input gracefully (e.g., non-numeric values for amounts).

Implementation Steps:
Start by defining a main function that will handle the user interaction.
Create a loop for the main menu that keeps running until the user chooses to exit.
Implement the functions required for each banking operation.
Ensure to maintain and update the user’s balance throughout the session.
