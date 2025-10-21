"""
Python Programming Concepts - Data Structures Exercise
Banking Application: Customer Data Management
"""

import csv
from collections import defaultdict

def read_customers_from_csv(filename):
    """Read customer data from CSV file and demonstrate different data structures"""
    
    # List to store all customer records
    customers_list = []
    
    # Dictionary to store customers by ID
    customers_dict = {}
    
    # Set to store unique account types
    account_types_set = set()
    
    # Tuple to store customer statistics
    customer_stats = (0, 0.0, 0)  # (count, total_balance, high_balance_count)
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Convert string values to appropriate types
                customer_data = {
                    'customer_id': int(row['customer_id']),
                    'name': row['name'],
                    'email': row['email'],
                    'phone': row['phone'],
                    'account_type': row['account_type'],
                    'balance': float(row['balance'])
                }
                
                # Add to list
                customers_list.append(customer_data)
                
                # Add to dictionary
                customers_dict[customer_data['customer_id']] = customer_data
                
                # Add account type to set
                account_types_set.add(customer_data['account_type'])
                
                # Update statistics
                total_balance = customer_stats[1] + customer_data['balance']
                high_balance_count = customer_stats[2] + (1 if customer_data['balance'] > 5000 else 0)
                customer_stats = (customer_stats[0] + 1, total_balance, high_balance_count)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None, None
    
    return customers_list, customers_dict, account_types_set, customer_stats

def demonstrate_data_structures():
    """Demonstrate different Python data structures with customer data"""
    
    print("=" * 60)
    print("🐍 PYTHON DATA STRUCTURES DEMONSTRATION")
    print("Banking Application - Customer Data Management")
    print("=" * 60)
    
    # Read customer data
    customers_list, customers_dict, account_types_set, customer_stats = read_customers_from_csv('../data/customers.csv')
    
    if customers_list is None:
        return
    
    print("\n1. LIST - All Customer Records:")
    print("-" * 40)
    for i, customer in enumerate(customers_list, 1):
        print(f"{i}. {customer['name']} ({customer['email']}) - {customer['account_type']} - ${customer['balance']:.2f}")
    
    print(f"\nTotal customers in list: {len(customers_list)}")
    
    print("\n2. DICTIONARY - Customer Lookup by ID:")
    print("-" * 40)
    for customer_id in sorted(customers_dict.keys()):
        customer = customers_dict[customer_id]
        print(f"ID {customer_id}: {customer['name']} - ${customer['balance']:.2f}")
    
    print("\n3. SET - Unique Account Types:")
    print("-" * 40)
    for account_type in sorted(account_types_set):
        print(f"• {account_type}")
    
    print("\n4. TUPLE - Customer Statistics:")
    print("-" * 40)
    count, total_balance, high_balance_count = customer_stats
    avg_balance = total_balance / count if count > 0 else 0
    print(f"Total Customers: {count}")
    print(f"Total Balance: ${total_balance:.2f}")
    print(f"Average Balance: ${avg_balance:.2f}")
    print(f"High Balance Customers (>$5000): {high_balance_count}")
    
    print("\n5. LIST COMPREHENSION - Filtering Examples:")
    print("-" * 40)
    
    # Customers with high balance
    high_balance_customers = [c for c in customers_list if c['balance'] > 5000]
    print(f"High Balance Customers: {len(high_balance_customers)}")
    for customer in high_balance_customers:
        print(f"  • {customer['name']}: ${customer['balance']:.2f}")
    
    # Savings account customers
    savings_customers = [c for c in customers_list if c['account_type'] == 'Savings']
    print(f"\nSavings Account Customers: {len(savings_customers)}")
    for customer in savings_customers:
        print(f"  • {customer['name']}: ${customer['balance']:.2f}")
    
    print("\n6. DICTIONARY COMPREHENSION - Account Type Summary:")
    print("-" * 40)
    account_summary = {
        account_type: len([c for c in customers_list if c['account_type'] == account_type])
        for account_type in account_types_set
    }
    
    for account_type, count in account_summary.items():
        print(f"{account_type}: {count} customers")
    
    print("\n7. NESTED DATA STRUCTURES - Customer Groups:")
    print("-" * 40)
    # Group customers by account type
    customers_by_type = defaultdict(list)
    for customer in customers_list:
        customers_by_type[customer['account_type']].append(customer)
    
    for account_type, customers in customers_by_type.items():
        print(f"\n{account_type} Account Holders:")
        for customer in customers:
            print(f"  • {customer['name']}: ${customer['balance']:.2f}")

if __name__ == "__main__":
    demonstrate_data_structures()
