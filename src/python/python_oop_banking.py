"""
Python Programming Concepts - Object-Oriented Programming
Banking Application: BankAccount and SavingsAccount Classes
"""

from datetime import datetime
import json

class BankAccount:
    """Base class for bank accounts with basic deposit and withdraw functionality"""
    
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        self.account_type = "Basic"
        self.created_date = datetime.now()
        
        # Add initial transaction if there's an initial balance
        if initial_balance > 0:
            self._add_transaction("Initial Deposit", initial_balance)
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return False
        
        self.balance += amount
        self._add_transaction("Deposit", amount)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: ${self.balance:.2f}")
            return False
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def get_balance(self):
        """Get current account balance"""
        return self.balance
    
    def get_account_info(self):
        """Get account information"""
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'account_type': self.account_type,
            'balance': self.balance,
            'created_date': self.created_date.strftime("%Y-%m-%d %H:%M:%S"),
            'transaction_count': len(self.transactions)
        }
    
    def get_transaction_history(self):
        """Get transaction history"""
        return self.transactions.copy()
    
    def _add_transaction(self, transaction_type, amount):
        """Add a transaction to the history"""
        transaction = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': transaction_type,
            'amount': amount,
            'balance_after': self.balance
        }
        self.transactions.append(transaction)
    
    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder} (${self.balance:.2f})"
    
    def __repr__(self):
        return f"BankAccount({self.account_number}, {self.account_holder}, {self.balance})"


class SavingsAccount(BankAccount):
    """Savings account with interest calculation and minimum balance requirements"""
    
    def __init__(self, account_number, account_holder, initial_balance=0.0, interest_rate=0.02, minimum_balance=100.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.account_type = "Savings"
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
        self.last_interest_date = datetime.now()
    
    def withdraw(self, amount):
        """Override withdraw to check minimum balance requirement"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        
        if amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: ${self.balance:.2f}")
            return False
        
        # Check if withdrawal would violate minimum balance
        if (self.balance - amount) < self.minimum_balance:
            print(f"Error: Withdrawal would violate minimum balance requirement of ${self.minimum_balance:.2f}")
            return False
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def calculate_interest(self):
        """Calculate and add interest to the account"""
        # Simple interest calculation (in real banking, this would be more complex)
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        self._add_transaction("Interest", interest_amount)
        self.last_interest_date = datetime.now()
        print(f"Interest of ${interest_amount:.2f} added. New balance: ${self.balance:.2f}")
        return interest_amount
    
    def get_interest_info(self):
        """Get interest-related information"""
        return {
            'interest_rate': self.interest_rate,
            'minimum_balance': self.minimum_balance,
            'last_interest_date': self.last_interest_date.strftime("%Y-%m-%d %H:%M:%S"),
            'projected_annual_interest': self.balance * self.interest_rate
        }
    
    def __str__(self):
        return f"Savings Account {self.account_number} - {self.account_holder} (${self.balance:.2f}) [Rate: {self.interest_rate:.1%}]"


class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_number, account_holder, initial_balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, account_holder, initial_balance)
        self.account_type = "Checking"
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Override withdraw to allow overdraft up to limit"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return False
        
        if amount > (self.balance + self.overdraft_limit):
            print(f"Error: Withdrawal exceeds available funds and overdraft limit.")
            print(f"Available: ${self.balance:.2f}, Overdraft limit: ${self.overdraft_limit:.2f}")
            return False
        
        self.balance -= amount
        self._add_transaction("Withdrawal", -amount)
        
        if self.balance < 0:
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f} (Overdraft: ${abs(self.balance):.2f})")
        else:
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return True
    
    def get_overdraft_info(self):
        """Get overdraft information"""
        return {
            'overdraft_limit': self.overdraft_limit,
            'available_balance': self.balance + self.overdraft_limit,
            'is_overdrawn': self.balance < 0
        }


def demonstrate_oop_concepts():
    """Demonstrate OOP concepts with banking examples"""
    
    print("=" * 60)
    print("🐍 PYTHON OOP CONCEPTS DEMONSTRATION")
    print("Banking Application - Account Management")
    print("=" * 60)
    
    # Create different types of accounts
    print("\n1. Creating Bank Accounts:")
    print("-" * 40)
    
    # Basic bank account
    basic_account = BankAccount("BA001", "John Smith", 1000.0)
    print(f"Created: {basic_account}")
    
    # Savings account
    savings_account = SavingsAccount("SA001", "Jane Doe", 5000.0, 0.03, 500.0)
    print(f"Created: {savings_account}")
    
    # Checking account
    checking_account = CheckingAccount("CA001", "Bob Johnson", 2000.0, 1000.0)
    print(f"Created: {checking_account}")
    
    print("\n2. Deposit Operations:")
    print("-" * 40)
    basic_account.deposit(500.0)
    savings_account.deposit(1000.0)
    checking_account.deposit(300.0)
    
    print("\n3. Withdrawal Operations:")
    print("-" * 40)
    basic_account.withdraw(200.0)
    savings_account.withdraw(300.0)
    checking_account.withdraw(500.0)
    
    print("\n4. Testing Savings Account Minimum Balance:")
    print("-" * 40)
    print(f"Current balance: ${savings_account.get_balance():.2f}")
    print(f"Minimum balance: ${savings_account.minimum_balance:.2f}")
    savings_account.withdraw(4800.0)  # This should fail due to minimum balance
    
    print("\n5. Testing Checking Account Overdraft:")
    print("-" * 40)
    print(f"Current balance: ${checking_account.get_balance():.2f}")
    print(f"Overdraft limit: ${checking_account.overdraft_limit:.2f}")
    checking_account.withdraw(1500.0)  # This should work with overdraft
    checking_account.withdraw(1000.0)  # This should fail
    
    print("\n6. Interest Calculation (Savings Account):")
    print("-" * 40)
    savings_account.calculate_interest()
    
    print("\n7. Account Information:")
    print("-" * 40)
    accounts = [basic_account, savings_account, checking_account]
    
    for account in accounts:
        print(f"\n{account.account_holder}'s Account:")
        info = account.get_account_info()
        for key, value in info.items():
            print(f"  {key.replace('_', ' ').title()}: {value}")
    
    print("\n8. Transaction History (Last 3 transactions per account):")
    print("-" * 40)
    
    for account in accounts:
        print(f"\n{account.account_holder}'s Transaction History:")
        transactions = account.get_transaction_history()
        for transaction in transactions[-3:]:  # Show last 3 transactions
            print(f"  {transaction['timestamp']}: {transaction['type']} ${transaction['amount']:.2f} (Balance: ${transaction['balance_after']:.2f})")
    
    print("\n9. Polymorphism Example - Account Processing:")
    print("-" * 40)
    
    def process_monthly_fee(account):
        """Process monthly fee for any account type"""
        if hasattr(account, 'account_type'):
            if account.account_type == "Savings":
                # No monthly fee for savings
                print(f"No monthly fee for {account.account_holder}'s savings account")
            elif account.account_type == "Checking":
                # $10 monthly fee for checking
                if account.withdraw(10.0):
                    print(f"Monthly fee of $10.00 processed for {account.account_holder}")
            else:
                # $5 monthly fee for basic accounts
                if account.withdraw(5.0):
                    print(f"Monthly fee of $5.00 processed for {account.account_holder}")
    
    for account in accounts:
        process_monthly_fee(account)
    
    print("\n10. Final Account Balances:")
    print("-" * 40)
    for account in accounts:
        print(f"{account}")


if __name__ == "__main__":
    demonstrate_oop_concepts()
