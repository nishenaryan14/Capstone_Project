# Banking Application - Python & SQL Implementation

## Selenium E2E Tests (nopCommerce Login)

### src/selenium_tests folder
- Dedicated examples per topic aligned with your list:
  - `tests/test_02_browser_driver_navigation.py`: Browser launching, driver methods, navigation
  - `tests/test_04_locators_06_webelement_methods.py`: Locators and WebElement methods
  - `tests/test_07_radio_09_checkbox_10_dropdown.py`: Radio, checkbox, dropdown
  - `tests/test_08_multiple_elements_autosuggest.py`: Multiple elements and auto-suggestion
  - `tests/test_11_web_table.py`: Web table (cart)
  - `tests/test_12_js_executor_13_scroll_14_screenshot.py`: JS executor, scroll, screenshot
  - `tests/test_15_hover_16_drag_rightclick.py`: Mouse hover, drag & drop, right click
  - `tests/test_17_window_18_frame_19_alerts.py`: Window, frame, alerts
  - `tests/test_20_waits.py`: Explicit waits

### End-to-End functional tests
- Run all e2e tests:
```bash
pytest -m e2e src/selenium_tests -q
```

- Flows covered:
  - Guest checkout from product page to order success
  - Register new user, login, logout
  - Search, add to wishlist/compare, add to cart, update/remove cart

Run only Selenium topics in this folder:
```bash
pytest src/selenium_tests -q
```

Prerequisites:
- Python 3.10+
- Google Chrome installed

Install dependencies:
```bash
pip install -r requirements.txt
```

Usage:
- Run all tests (headless by default):
```bash
pytest -q
```

- Show browser (disable headless):
```bash
set HEADLESS=false && pytest -q
```

- Target a single file or test:
```bash
pytest tests/test_login_basic.py::test_invalid_login_shows_error -q
```

Environment variables:
- `BASE_URL` (default: `https://demo.nopcommerce.com`)
- `HEADLESS` set to `true|false` (default: `true`)

Test coverage:
- Invalid login shows summary error
- Empty fields show inline validation
- Forgot password navigation
- UI elements presence and Remember me checkbox behavior

This project demonstrates Python programming concepts and SQL database operations for a banking application.

## Project Structure

```
├── main.py                         # Main application launcher
├── src/
│   ├── python/                     # Python source code
│   │   ├── main_menu.py           # Main menu interface program
│   │   ├── python_data_structures.py  # Data structures demonstration
│   │   ├── python_oop_banking.py     # Object-Oriented Programming examples
│   │   └── run_banking_app.py        # Alternative launcher script
│   └── sql/                        # SQL database files
│       ├── sql_banking_database.sql   # Complete SQL database schema
│       └── sql_essential_queries.sql  # Essential SQL queries
├── data/                           # Data files
│   └── customers.csv               # Sample customer data
└── docs/                           # Documentation
    └── README.md                   # This file
```

## 🚀 Quick Start - Menu Interface

**Recommended way to run the application:**
```bash
python main.py
```

**Alternative launcher:**
```bash
python src/python/run_banking_app.py
```

## 🎮 Menu Interface Features

The main menu provides a user-friendly interface with the following options:

### 🐍 Python Programming Concepts:
1. **Data Structures Exercise** - Lists, Tuples, Sets, Dictionaries
2. **Object-Oriented Programming** - BankAccount & SavingsAccount classes
3. **Interactive Banking Simulation** - Hands-on account management
4. **Data Analysis & Statistics** - Customer data analytics

### 🗄️ SQL Database Operations:
5. **View SQL Database Schema** - Display database structure
6. **View Essential SQL Queries** - Show available SQL operations
7. **Database Connection Test** - Test database connectivity

### 🔧 Utilities:
8. **View Project Documentation** - Display README and project info
9. **Run All Python Exercises** - Execute all Python demos sequentially
0. **Exit Program** - Quit the application

## Python Programming Concepts

### 1. Data Structures Exercise (`python_data_structures.py`)

**Features:**
- Reads customer data from CSV file
- Demonstrates Python data structures:
  - **List**: Stores all customer records
  - **Dictionary**: Customer lookup by ID
  - **Set**: Unique account types
  - **Tuple**: Customer statistics
- Shows list comprehensions and dictionary comprehensions
- Demonstrates nested data structures

**To run:**
```bash
python src/python/python_data_structures.py
```

### 2. Object-Oriented Programming (`python_oop_banking.py`)

**Features:**
- **BankAccount class**: Base class with deposit/withdraw methods
- **SavingsAccount class**: Extends BankAccount with interest calculation and minimum balance
- **CheckingAccount class**: Extends BankAccount with overdraft protection
- Demonstrates inheritance, polymorphism, and encapsulation
- Shows transaction history and account management

**To run:**
```bash
python src/python/python_oop_banking.py
```

## SQL Database Operations

### 1. Complete Database Schema (`sql_banking_database.sql`)

**Features:**
- Complete database schema with all tables
- Sample data insertion
- Advanced stored procedures
- Complex analytical queries
- Transaction processing procedures

### 2. Essential Queries (`sql_essential_queries.sql`)

**Features:**
- Simplified database schema
- Basic CRUD operations (SELECT, UPDATE, DELETE)
- JOIN queries between Customer and Orders tables
- Active Customers view
- Stored procedure for adding new customers

**To run:**
```sql
-- Execute in MySQL/MariaDB
source sql_essential_queries.sql;
```

## Database Tables

### Core Tables:
- **Customers**: Customer information
- **Accounts**: Bank accounts (checking, savings, etc.)
- **Transactions**: Account transactions
- **Orders**: Banking services (loans, credit cards, etc.)

### Key Features:
- Foreign key relationships
- Data integrity constraints
- Timestamp tracking
- Active/inactive status management

## SQL Operations Demonstrated

### 1. Basic Queries
- SELECT with various conditions
- UPDATE operations
- DELETE operations
- Data filtering and sorting

### 2. JOIN Operations
- Customer + Orders relationships
- Complex multi-table joins
- Aggregate functions with grouping

### 3. Views
- **ActiveCustomers**: Summary view of active customers with account and order statistics

### 4. Stored Procedures
- **AddNewCustomer**: Complete customer creation with account setup
- **ProcessDeposit**: Transaction processing with balance updates
- **ProcessWithdrawal**: Withdrawal processing with balance validation

## Sample Data

The project includes sample data for:
- 8 customers with various account types
- Multiple account types (checking, savings, money market, CD)
- Transaction history
- Banking service orders (loans, credit cards, mortgages)

## Usage Examples

### Python Data Structures
```python
# Demonstrates various Python data structures
customers_list, customers_dict, account_types_set, customer_stats = read_customers_from_csv('customers.csv')
```

### Python OOP
```python
# Create different account types
savings_account = SavingsAccount("SA001", "Jane Doe", 5000.0, 0.03, 500.0)
checking_account = CheckingAccount("CA001", "Bob Johnson", 2000.0, 1000.0)
```

### SQL Queries
```sql
-- Get customers with their accounts
SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS full_name,
       a.account_number, a.balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id;

-- Use the stored procedure
CALL AddNewCustomer('Michael', 'Johnson', 'michael.johnson@email.com', '555-0201', 1000.00);
```

## Requirements

### Python:
- Python 3.6+
- No external dependencies required

### SQL:
- MySQL 5.7+ or MariaDB 10.2+
- Database user with CREATE, INSERT, UPDATE, DELETE privileges

## Next Steps

After running both Python and SQL components separately, you can consider:
1. Integrating Python with SQL using database connectors
2. Creating a web interface using Flask/Django
3. Adding REST API endpoints
4. Implementing real-time transaction processing
5. Adding data validation and error handling

## Notes

- All code is production-ready with proper error handling
- SQL queries include transaction safety
- Python classes follow OOP best practices
- Database schema supports real-world banking scenarios
