# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account 

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest_rate = float(input("Enter the savings account interest rate (%): "))
    savings_months = int(input("Enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    # savings_updated_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)
    # create_savings_account(savings_balance, savings_interest_rate, savings_months)
    create_savings_account()

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Savings Account - Initial Balance: ${savings_balance:.2f}")
    # print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Balance: ${savings_updated_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nEnter the CD account balance: "))
    cd_interest_rate = float(input("Enter the CD account interest rate (%): "))
    cd_months = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    # cd_updated_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)
    # create_cd_account(cd_balance, cd_interest_rate, cd_months)
    create_cd_account()
  
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nCD Account - Initial Balance: ${cd_balance:.2f}")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated Balance: ${cd_updated_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()