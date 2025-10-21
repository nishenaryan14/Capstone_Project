"""
Banking Application - Main Menu Interface
Python Programming Concepts & SQL Database Operations
"""

import os
import sys
from datetime import datetime

def display_header():
    """Display the main header"""
    print("=" * 70)
    print("🏦 BANKING APPLICATION - PYTHON & SQL IMPLEMENTATION")
    print("=" * 70)
    print("Python Programming Concepts & SQL Database Operations")
    print("=" * 70)

def display_main_menu():
    """Display the main menu options"""
    print("\n📋 MAIN MENU - Choose an option:")
    print("-" * 50)
    print("🐍 PYTHON PROGRAMMING CONCEPTS:")
    print("   1. Data Structures Exercise (Lists, Tuples, Sets, Dictionaries)")
    print("   2. Object-Oriented Programming (BankAccount & SavingsAccount)")
    print("   3. Interactive Banking Simulation")
    print("   4. Data Analysis & Statistics")
    print("")
    print("🗄️  SQL DATABASE OPERATIONS:")
    print("   5. View SQL Database Schema")
    print("   6. View Essential SQL Queries")
    print("   7. Database Connection Test (if configured)")
    print("")
    print("🔧 UTILITIES:")
    print("   8. View Project Documentation")
    print("   9. Run All Python Exercises")
    print("   0. Exit Program")
    print("-" * 50)

def get_user_choice():
    """Get user choice with validation"""
    while True:
        try:
            choice = input("\n🎯 Enter your choice (0-9): ").strip()
            if choice.isdigit() and 0 <= int(choice) <= 9:
                return int(choice)
            else:
                print("❌ Invalid choice! Please enter a number between 0-9.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")

def run_data_structures():
    """Run the data structures exercise"""
    print("\n" + "="*60)
    print("🐍 PYTHON DATA STRUCTURES EXERCISE")
    print("="*60)
    
    try:
        # Import and run the data structures module
        from .python_data_structures import demonstrate_data_structures
        demonstrate_data_structures()
    except ImportError as e:
        print(f"❌ Error importing data structures module: {e}")
    except Exception as e:
        print(f"❌ Error running data structures exercise: {e}")

def run_oop_exercise():
    """Run the OOP exercise"""
    print("\n" + "="*60)
    print("🐍 PYTHON OOP EXERCISE")
    print("="*60)
    
    try:
        # Import and run the OOP module
        from .python_oop_banking import demonstrate_oop_concepts
        demonstrate_oop_concepts()
    except ImportError as e:
        print(f"❌ Error importing OOP module: {e}")
    except Exception as e:
        print(f"❌ Error running OOP exercise: {e}")

def run_interactive_banking():
    """Run interactive banking simulation"""
    print("\n" + "="*60)
    print("🏦 INTERACTIVE BANKING SIMULATION")
    print("="*60)
    
    try:
        from .python_oop_banking import BankAccount, SavingsAccount, CheckingAccount
        
        print("Welcome to Interactive Banking Simulation!")
        print("Let's create some accounts and perform transactions.\n")
        
        # Create sample accounts
        accounts = []
        
        # Create a basic account
        basic_account = BankAccount("BA001", "Demo User", 1000.0)
        accounts.append(basic_account)
        print(f"✅ Created: {basic_account}")
        
        # Create a savings account
        savings_account = SavingsAccount("SA001", "Demo Saver", 5000.0, 0.03, 500.0)
        accounts.append(savings_account)
        print(f"✅ Created: {savings_account}")
        
        # Create a checking account
        checking_account = CheckingAccount("CA001", "Demo Checker", 2000.0, 1000.0)
        accounts.append(checking_account)
        print(f"✅ Created: {checking_account}")
        
        print("\n🎮 Interactive Menu:")
        while True:
            print("\n" + "-"*40)
            print("Choose an action:")
            print("1. Deposit money")
            print("2. Withdraw money")
            print("3. View account info")
            print("4. Calculate interest (Savings only)")
            print("5. View transaction history")
            print("6. Back to main menu")
            
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == "1":
                account_choice = get_account_choice(accounts)
                if account_choice is not None:
                    amount = get_amount("deposit")
                    if amount > 0:
                        accounts[account_choice].deposit(amount)
            
            elif choice == "2":
                account_choice = get_account_choice(accounts)
                if account_choice is not None:
                    amount = get_amount("withdraw")
                    if amount > 0:
                        accounts[account_choice].withdraw(amount)
            
            elif choice == "3":
                account_choice = get_account_choice(accounts)
                if account_choice is not None:
                    info = accounts[account_choice].get_account_info()
                    print(f"\n📊 Account Information:")
                    for key, value in info.items():
                        print(f"   {key.replace('_', ' ').title()}: {value}")
            
            elif choice == "4":
                savings_accounts = [i for i, acc in enumerate(accounts) if isinstance(acc, SavingsAccount)]
                if savings_accounts:
                    print(f"\n💰 Calculating interest for savings account...")
                    savings_account.calculate_interest()
                else:
                    print("❌ No savings accounts available for interest calculation.")
            
            elif choice == "5":
                account_choice = get_account_choice(accounts)
                if account_choice is not None:
                    transactions = accounts[account_choice].get_transaction_history()
                    print(f"\n📜 Transaction History:")
                    for i, transaction in enumerate(transactions[-5:], 1):  # Show last 5
                        print(f"   {i}. {transaction['timestamp']}: {transaction['type']} ${transaction['amount']:.2f}")
            
            elif choice == "6":
                break
            
            else:
                print("❌ Invalid choice! Please enter 1-6.")
    
    except Exception as e:
        print(f"❌ Error in interactive banking: {e}")

def get_account_choice(accounts):
    """Get user's account choice"""
    print(f"\nSelect an account:")
    for i, account in enumerate(accounts):
        print(f"   {i+1}. {account}")
    
    while True:
        try:
            choice = int(input("Enter account number (1-{}): ".format(len(accounts))))
            if 1 <= choice <= len(accounts):
                return choice - 1
            else:
                print("❌ Invalid choice!")
        except ValueError:
            print("❌ Please enter a valid number!")

def get_amount(action):
    """Get amount from user"""
    while True:
        try:
            amount = float(input(f"Enter amount to {action}: $"))
            if amount > 0:
                return amount
            else:
                print("❌ Amount must be positive!")
        except ValueError:
            print("❌ Please enter a valid number!")

def run_data_analysis():
    """Run data analysis and statistics"""
    print("\n" + "="*60)
    print("📊 DATA ANALYSIS & STATISTICS")
    print("="*60)
    
    try:
        from .python_data_structures import read_customers_from_csv
        
        # Read customer data
        customers_list, customers_dict, account_types_set, customer_stats = read_customers_from_csv('../data/customers.csv')
        
        if customers_list is None:
            print("❌ Could not load customer data.")
            return
        
        print("📈 CUSTOMER DATA ANALYSIS")
        print("-" * 40)
        
        # Basic statistics
        count, total_balance, high_balance_count = customer_stats
        avg_balance = total_balance / count if count > 0 else 0
        
        print(f"📊 Customer Statistics:")
        print(f"   Total Customers: {count}")
        print(f"   Total Balance: ${total_balance:,.2f}")
        print(f"   Average Balance: ${avg_balance:,.2f}")
        print(f"   High Balance Customers (>$5000): {high_balance_count}")
        
        # Account type analysis
        print(f"\n🏦 Account Type Distribution:")
        account_summary = {}
        for customer in customers_list:
            account_type = customer['account_type']
            account_summary[account_type] = account_summary.get(account_type, 0) + 1
        
        for account_type, count in account_summary.items():
            percentage = (count / len(customers_list)) * 100
            print(f"   {account_type}: {count} customers ({percentage:.1f}%)")
        
        # Balance analysis
        balances = [customer['balance'] for customer in customers_list]
        balances.sort(reverse=True)
        
        print(f"\n💰 Balance Analysis:")
        print(f"   Highest Balance: ${max(balances):,.2f}")
        print(f"   Lowest Balance: ${min(balances):,.2f}")
        print(f"   Median Balance: ${balances[len(balances)//2]:,.2f}")
        
        # Top customers
        print(f"\n🏆 Top 3 Customers by Balance:")
        for i, customer in enumerate(sorted(customers_list, key=lambda x: x['balance'], reverse=True)[:3], 1):
            print(f"   {i}. {customer['name']}: ${customer['balance']:,.2f} ({customer['account_type']})")
        
    except Exception as e:
        print(f"❌ Error in data analysis: {e}")

def view_sql_schema():
    """Display SQL database schema"""
    print("\n" + "="*60)
    print("🗄️  SQL DATABASE SCHEMA")
    print("="*60)
    
    try:
        with open('../sql/sql_banking_database.sql', 'r') as file:
            content = file.read()
            
        # Extract and display table creation statements
        lines = content.split('\n')
        in_create_section = False
        
        print("📋 Database Tables:")
        print("-" * 40)
        
        for line in lines:
            if 'CREATE TABLE' in line.upper():
                table_name = line.split()[2] if len(line.split()) > 2 else "Unknown"
                print(f"   📊 {table_name}")
            elif 'CREATE VIEW' in line.upper():
                view_name = line.split()[2] if len(line.split()) > 2 else "Unknown"
                print(f"   👁️  {view_name} (View)")
            elif 'CREATE PROCEDURE' in line.upper():
                proc_name = line.split()[2] if len(line.split()) > 2 else "Unknown"
                print(f"   ⚙️  {proc_name} (Stored Procedure)")
        
        print(f"\n📁 Files available:")
        print(f"   • sql_banking_database.sql (Complete schema)")
        print(f"   • sql_essential_queries.sql (Essential queries)")
        
    except FileNotFoundError:
        print("❌ SQL files not found in current directory.")
    except Exception as e:
        print(f"❌ Error reading SQL schema: {e}")

def view_sql_queries():
    """Display essential SQL queries"""
    print("\n" + "="*60)
    print("🗄️  ESSENTIAL SQL QUERIES")
    print("="*60)
    
    try:
        with open('../sql/sql_essential_queries.sql', 'r') as file:
            content = file.read()
        
        # Extract query sections
        sections = [
            ("CREATE TABLES", "CREATE TABLE"),
            ("INSERT DATA", "INSERT INTO"),
            ("SELECT QUERIES", "-- SELECT:"),
            ("UPDATE QUERIES", "-- UPDATE:"),
            ("DELETE QUERIES", "-- DELETE:"),
            ("JOIN QUERIES", "-- JOIN"),
            ("VIEWS", "CREATE VIEW"),
            ("STORED PROCEDURES", "CREATE PROCEDURE")
        ]
        
        print("📋 Available Query Categories:")
        print("-" * 40)
        
        for section_name, marker in sections:
            if marker in content:
                print(f"   ✅ {section_name}")
            else:
                print(f"   ❌ {section_name}")
        
        print(f"\n💡 To execute these queries:")
        print(f"   1. Open MySQL/MariaDB command line")
        print(f"   2. Run: source sql_essential_queries.sql;")
        print(f"   3. Or copy and paste individual queries")
        
    except FileNotFoundError:
        print("❌ SQL essential queries file not found.")
    except Exception as e:
        print(f"❌ Error reading SQL queries: {e}")

def view_documentation():
    """Display project documentation"""
    print("\n" + "="*60)
    print("📚 PROJECT DOCUMENTATION")
    print("="*60)
    
    try:
        with open('../docs/README.md', 'r') as file:
            content = file.read()
        
        # Display key sections
        lines = content.split('\n')
        in_section = False
        
        for line in lines:
            if line.startswith('##') or line.startswith('###'):
                print(f"\n{line}")
                in_section = True
            elif line.startswith('#') and not line.startswith('##'):
                print(f"\n{line}")
                in_section = True
            elif in_section and line.strip() and not line.startswith('#'):
                print(line)
            elif line.strip() == '':
                in_section = False
        
        print(f"\n📁 Project Files:")
        files = [
            "customers.csv - Sample customer data",
            "python_data_structures.py - Data structures exercise",
            "python_oop_banking.py - OOP banking classes",
            "sql_banking_database.sql - Complete database schema",
            "sql_essential_queries.sql - Essential SQL queries",
            "main_menu.py - This menu program"
        ]
        
        for file_info in files:
            print(f"   📄 {file_info}")
        
    except FileNotFoundError:
        print("❌ README.md file not found.")
    except Exception as e:
        print(f"❌ Error reading documentation: {e}")

def run_all_python_exercises():
    """Run all Python exercises in sequence"""
    print("\n" + "="*60)
    print("🚀 RUNNING ALL PYTHON EXERCISES")
    print("="*60)
    
    exercises = [
        ("Data Structures", run_data_structures),
        ("OOP Concepts", run_oop_exercise),
        ("Data Analysis", run_data_analysis)
    ]
    
    for i, (name, func) in enumerate(exercises, 1):
        print(f"\n{'='*20} EXERCISE {i}: {name.upper()} {'='*20}")
        try:
            func()
        except Exception as e:
            print(f"❌ Error in {name}: {e}")
        
        if i < len(exercises):
            input(f"\n⏸️  Press Enter to continue to next exercise...")
    
    print(f"\n✅ All Python exercises completed!")

def main():
    """Main program loop"""
    while True:
        try:
            # Clear screen (works on Windows and Unix)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            display_header()
            display_main_menu()
            
            choice = get_user_choice()
            
            if choice == 0:
                print("\n👋 Thank you for using the Banking Application!")
                print("Goodbye! 🏦")
                break
            
            elif choice == 1:
                run_data_structures()
            
            elif choice == 2:
                run_oop_exercise()
            
            elif choice == 3:
                run_interactive_banking()
            
            elif choice == 4:
                run_data_analysis()
            
            elif choice == 5:
                view_sql_schema()
            
            elif choice == 6:
                view_sql_queries()
            
            elif choice == 7:
                print("\n🔌 Database Connection Test")
                print("-" * 40)
                print("💡 To test database connection:")
                print("   1. Install MySQL connector: pip install mysql-connector-python")
                print("   2. Configure database connection in your code")
                print("   3. Run database connection test")
                print("\n📝 Example connection code:")
                print("""
import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='BankingDB'
    )
    print("✅ Database connection successful!")
    connection.close()
except Exception as e:
    print(f"❌ Database connection failed: {e}")
                """)
            
            elif choice == 8:
                view_documentation()
            
            elif choice == 9:
                run_all_python_exercises()
            
            # Wait for user to continue
            if choice != 0:
                input(f"\n⏸️  Press Enter to return to main menu...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
