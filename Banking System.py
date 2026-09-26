from abc import ABC, abstractmethod
from datetime import datetime


# Abstraction
class Account(ABC):

    def __init__(self, account_number, name, balance=0.0):
        self._account_number = account_number
        self._name = name
        self._balance = balance
        self._transactions = []

    # Encapsulation
    @property
    def account_number(self):
        return self._account_number

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self._balance += amount
        self._add_transaction(f"Deposited Rs.{amount:.2f}")
        print(f"Rs.{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self._balance:
            print("Insufficient balance.")
            return

        self._balance -= amount
        self._add_transaction(f"Withdrew Rs.{amount:.2f}")
        print(f"Rs.{amount:.2f} withdrawn successfully.")

    def _add_transaction(self, message):
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self._transactions.append(f"{time} - {message}")

    def show_transactions(self):
        print("\n----- Transaction History -----")

        if not self._transactions:
            print("No transactions available.")
            return

        for transaction in self._transactions:
            print(transaction)

    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Account Type   : {self.account_type()}")
        print(f"Balance        : Rs.{self.balance:.2f}")

    # Abstract method
    @abstractmethod
    def account_type(self):
        pass


# Inheritance
class SavingsAccount(Account):

    # Polymorphism
    def account_type(self):
        return "Savings Account"

    def add_interest(self):
        interest_rate = 4.0
        interest = self._balance * interest_rate / 100

        self._balance += interest
        self._add_transaction(
            f"Interest added Rs.{interest:.2f}"
        )

        print(f"Interest of Rs.{interest:.2f} added successfully.")


class CurrentAccount(Account):

    # Polymorphism
    def account_type(self):
        return "Current Account"


def create_account(accounts):
    print("\n----- Create Account -----")

    account_number = input("Enter account number: ").strip()

    if not account_number:
        print("Account number cannot be empty.")
        return

    if account_number in accounts:
        print("Account number already exists.")
        return

    name = input("Enter account holder name: ").strip()

    if not name:
        print("Account holder name cannot be empty.")
        return

    print("\n1. Savings Account")
    print("2. Current Account")

    choice = input("Choose account type: ").strip()

    if choice == "1":
        account = SavingsAccount(account_number, name)

    elif choice == "2":
        account = CurrentAccount(account_number, name)

    else:
        print("Invalid account type.")
        return

    accounts[account_number] = account

    print("Account created successfully.")


def find_account(accounts):
    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("Account not found.")
        return None

    return accounts[account_number]


def main():

    accounts = {}

    while True:

        print("\n========== PYTHON BANKING SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Account Details")
        print("5. View Transaction History")
        print("6. Add Interest to Savings Account")
        print("7. Exit")
        print("===========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            account = find_account(accounts)

            if account:
                try:
                    amount = float(
                        input("Enter deposit amount: ")
                    )
                    account.deposit(amount)

                except ValueError:
                    print("Please enter a valid amount.")

        elif choice == "3":
            account = find_account(accounts)

            if account:
                try:
                    amount = float(
                        input("Enter withdrawal amount: ")
                    )
                    account.withdraw(amount)

                except ValueError:
                    print("Please enter a valid amount.")

        elif choice == "4":
            account = find_account(accounts)

            if account:
                account.show_details()

        elif choice == "5":
            account = find_account(accounts)

            if account:
                account.show_transactions()

        elif choice == "6":
            account = find_account(accounts)

            if account:

                if isinstance(account, SavingsAccount):
                    account.add_interest()

                else:
                    print(
                        "Interest is available only for Savings Accounts."
                    )

        elif choice == "7":
            print(
                "Thank you for using the Python Banking System!"
            )
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
