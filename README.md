# customer_banking
Module 3 Challenge

Sergio's Savings & Desposit Bank

Overview:

This repository contains Python code for a simple banking system, with classes representing a general account, a certificate of deposit (CD) account, and a savings account. The system allows users to set initial balances, interest rates, and periods, and then calculates the interest earned and updates the account balances accordingly.

Files:

Account.py

This file defines the Account class, which serves as a generic bank account. The class has an initializer (__init__) that sets the initial balance and interest for the account. It also provides methods (set_balance and set_interest) to update the balance and interest of the account.

cd_account.py

This file implements the CDAccount class, a specialized type of account representing a certificate of deposit (CD). The CDAccount class inherits from the Account class and introduces additional methods. Notably, it includes a calculate_interest method for computing the interest earned based on the balance and interest rate, and an update_balance_and_interest method to update the balance and interest together.

Savings_account.py

Similar to cd_account.py, this file implements the SavingsAccount class, representing a savings account. The structure mirrors that of the CDAccount class, with methods for calculating interest and updating the account balance.

customer_banking.py

The main script for user interaction. It imports the CDAccount and SavingsAccount classes, prompts the user to input information for both account types (initial balance, interest rate, and months), and then calls the relevant methods to calculate interest and update balances. Finally, it prints out the results, including the initial balance, interest earned, and updated balance for both the CD and savings accounts.

The script acts as a simple interface for users to simulate interactions with the banking system, providing a way to input account details and see the impact of interest on account balances over time.

Instructions:

1.  Clone the repository.
2.  Run customer_banking.py to simulate earning interest within the banking system.
