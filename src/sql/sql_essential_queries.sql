-- =============================================
-- BANKING APPLICATION - ESSENTIAL SQL QUERIES
-- Complete implementation covering all requirements
-- =============================================

-- =============================================
-- 1. CREATE DATABASE TABLES
-- =============================================

-- Create the main database
CREATE DATABASE IF NOT EXISTS BankingDB;
USE BankingDB;

-- Drop existing tables if they exist 
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
DROP VIEW IF EXISTS ActiveCustomers;
DROP PROCEDURE IF EXISTS AddNewCustomer;
DROP PROCEDURE IF EXISTS ProcessDeposit;
DROP PROCEDURE IF EXISTS ProcessWithdrawal;

-- Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Accounts table
CREATE TABLE Accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    account_number VARCHAR(20) UNIQUE NOT NULL,
    account_type VARCHAR(20) NOT NULL,
    balance DECIMAL(15,2) DEFAULT 0.00,
    opened_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Transactions table
CREATE TABLE Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    transaction_type VARCHAR(20) NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    description TEXT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    balance_after DECIMAL(15,2) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);

-- Orders table (for banking services like loans, credit cards, etc.)
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_type VARCHAR(20) NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING',
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved_date TIMESTAMP NULL,
    description TEXT,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- =============================================
-- 2. INSERT SAMPLE DATA
-- =============================================

-- Insert Customers
INSERT INTO Customers (first_name, last_name, email, phone, date_of_birth, address, city, state, zip_code) VALUES
('John', 'Smith', 'john.smith@email.com', '555-0101', '1985-03-15', '123 Main St', 'New York', 'NY', '10001'),
('Jane', 'Doe', 'jane.doe@email.com', '555-0102', '1990-07-22', '456 Oak Ave', 'Los Angeles', 'CA', '90210'),
('Bob', 'Johnson', 'bob.johnson@email.com', '555-0103', '1978-11-08', '789 Pine Rd', 'Chicago', 'IL', '60601'),
('Alice', 'Brown', 'alice.brown@email.com', '555-0104', '1992-01-30', '321 Elm St', 'Houston', 'TX', '77001'),
('Charlie', 'Wilson', 'charlie.wilson@email.com', '555-0105', '1988-09-12', '654 Maple Dr', 'Phoenix', 'AZ', '85001'),
('Diana', 'Prince', 'diana.prince@email.com', '555-0106', '1983-05-18', '987 Cedar Ln', 'Philadelphia', 'PA', '19101'),
('Frank', 'Miller', 'frank.miller@email.com', '555-0107', '1975-12-03', '147 Birch St', 'San Antonio', 'TX', '78201'),
('Grace', 'Lee', 'grace.lee@email.com', '555-0108', '1995-04-25', '258 Spruce Ave', 'San Diego', 'CA', '92101');

-- Insert Accounts
INSERT INTO Accounts (customer_id, account_number, account_type, balance) VALUES
(1, 'CHK001', 'CHECKING', 2500.00),
(1, 'SAV001', 'SAVINGS', 5000.00),
(2, 'CHK002', 'CHECKING', 1200.00),
(2, 'SAV002', 'SAVINGS', 8000.00),
(3, 'CHK003', 'CHECKING', 3500.00),
(4, 'CHK004', 'CHECKING', 800.00),
(5, 'CHK005', 'CHECKING', 4500.00),
(6, 'CHK006', 'CHECKING', 2200.00),
(7, 'CHK007', 'CHECKING', 5000.00),
(8, 'CHK008', 'CHECKING', 600.00);

-- Insert initial transactions
INSERT INTO Transactions (account_id, transaction_type, amount, description, balance_after) VALUES
(1, 'DEPOSIT', 2500.00, 'Initial deposit', 2500.00),
(2, 'DEPOSIT', 5000.00, 'Initial deposit', 5000.00),
(3, 'DEPOSIT', 1200.00, 'Initial deposit', 1200.00),
(4, 'DEPOSIT', 8000.00, 'Initial deposit', 8000.00),
(5, 'DEPOSIT', 3500.00, 'Initial deposit', 3500.00),
(6, 'DEPOSIT', 800.00, 'Initial deposit', 800.00),
(7, 'DEPOSIT', 4500.00, 'Initial deposit', 4500.00),
(8, 'DEPOSIT', 2200.00, 'Initial deposit', 2200.00),
(9, 'DEPOSIT', 5000.00, 'Initial deposit', 5000.00),
(10, 'DEPOSIT', 600.00, 'Initial deposit', 600.00);

-- Insert Orders
INSERT INTO Orders (customer_id, order_type, amount, status, description) VALUES
(1, 'LOAN', 15000.00, 'APPROVED', 'Personal loan for home improvement'),
(2, 'CREDIT_CARD', 5000.00, 'APPROVED', 'Credit card application'),
(3, 'MORTGAGE', 300000.00, 'PENDING', 'Home mortgage application'),
(4, 'LOAN', 8000.00, 'REJECTED', 'Auto loan application'),
(5, 'INVESTMENT', 25000.00, 'APPROVED', 'Investment account opening'),
(6, 'CREDIT_CARD', 10000.00, 'APPROVED', 'Premium credit card'),
(7, 'MORTGAGE', 500000.00, 'APPROVED', 'Luxury home mortgage'),
(8, 'LOAN', 3000.00, 'PENDING', 'Student loan refinancing');

-- =============================================
-- 3. BASIC QUERIES (SELECT, UPDATE, DELETE)
-- =============================================

-- SELECT QUERIES
-- Get all customers
SELECT '=== ALL CUSTOMERS ===' AS Query_Type;
SELECT customer_id, first_name, last_name, email, phone, created_date 
FROM Customers 
ORDER BY last_name, first_name;

-- Get customers with their account information
SELECT '=== CUSTOMERS WITH ACCOUNTS ===' AS Query_Type;
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.email,
    a.account_number,
    a.account_type,
    a.balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
ORDER BY c.last_name, c.first_name;

-- Get high balance accounts (>$3000)
SELECT '=== HIGH BALANCE ACCOUNTS ===' AS Query_Type;
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    a.account_number,
    a.account_type,
    a.balance
FROM Customers c
JOIN Accounts a ON c.customer_id = a.customer_id
WHERE a.balance > 3000.00
ORDER BY a.balance DESC;

-- Get transaction history for account 1
SELECT '=== TRANSACTION HISTORY FOR ACCOUNT 1 ===' AS Query_Type;
SELECT 
    t.transaction_id,
    t.transaction_type,
    t.amount,
    t.description,
    t.transaction_date,
    t.balance_after
FROM Transactions t
WHERE t.account_id = 1
ORDER BY t.transaction_date DESC;

-- UPDATE QUERIES
-- Update customer phone number
SELECT '=== UPDATING CUSTOMER PHONE ===' AS Query_Type;
UPDATE Customers 
SET phone = '555-9999' 
WHERE customer_id = 1;

-- Verify the update
SELECT customer_id, first_name, last_name, phone 
FROM Customers 
WHERE customer_id = 1;

-- Update account balance
SELECT '=== UPDATING ACCOUNT BALANCE ===' AS Query_Type;
UPDATE Accounts 
SET balance = balance + 500.00 
WHERE account_id = 1;

-- Verify the balance update
SELECT account_id, account_number, balance 
FROM Accounts 
WHERE account_id = 1;

-- Update order status
SELECT '=== UPDATING ORDER STATUS ===' AS Query_Type;
UPDATE Orders 
SET status = 'APPROVED', approved_date = CURRENT_TIMESTAMP 
WHERE order_id = 3;

-- Verify the order update
SELECT order_id, customer_id, order_type, status, approved_date 
FROM Orders 
WHERE order_id = 3;

-- DELETE QUERIES
-- Delete rejected orders
SELECT '=== DELETING REJECTED ORDERS ===' AS Query_Type;
SELECT COUNT(*) AS orders_before_delete FROM Orders WHERE status = 'REJECTED';

DELETE FROM Orders WHERE status = 'REJECTED';

SELECT COUNT(*) AS orders_after_delete FROM Orders WHERE status = 'REJECTED';

-- =============================================
-- 4. JOIN QUERY (Customer + Orders table)
-- =============================================

SELECT '=== CUSTOMER + ORDERS JOIN QUERY ===' AS Query_Type;

-- Get customers with their orders
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    o.order_id,
    o.order_type,
    o.amount AS order_amount,
    o.status,
    o.order_date
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
ORDER BY c.last_name, o.order_date DESC;

-- Get customers with total order amounts
SELECT '=== CUSTOMERS WITH TOTAL ORDER AMOUNTS ===' AS Query_Type;
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_order_amount,
    COALESCE(AVG(o.amount), 0) AS average_order_amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_order_amount DESC;

-- Get customers with approved orders only
SELECT '=== CUSTOMERS WITH APPROVED ORDERS ===' AS Query_Type;
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    o.order_type,
    o.amount,
    o.approved_date
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
WHERE o.status = 'APPROVED'
ORDER BY o.approved_date DESC;

-- =============================================
-- 5. CREATE VIEW: Active Customers
-- =============================================

SELECT '=== CREATING ACTIVE CUSTOMERS VIEW ===' AS Query_Type;

CREATE VIEW ActiveCustomers AS
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.email,
    c.phone,
    c.created_date,
    COUNT(a.account_id) AS total_accounts,
    COALESCE(SUM(a.balance), 0) AS total_balance,
    COUNT(o.order_id) AS total_orders,
    MAX(a.opened_date) AS last_account_opened
FROM Customers c
LEFT JOIN Accounts a ON c.customer_id = a.customer_id AND a.is_active = TRUE
LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE c.is_active = TRUE
GROUP BY c.customer_id, c.first_name, c.last_name, c.email, c.phone, c.created_date;

-- Query the view
SELECT '=== QUERYING ACTIVE CUSTOMERS VIEW ===' AS Query_Type;
SELECT * FROM ActiveCustomers ORDER BY total_balance DESC;

-- =============================================
-- 6. STORED PROCEDURE: Add new customer
-- =============================================

SELECT '=== CREATING ADD NEW CUSTOMER PROCEDURE ===' AS Query_Type;

DELIMITER //

CREATE PROCEDURE AddNewCustomer(
    IN p_first_name VARCHAR(50),
    IN p_last_name VARCHAR(50),
    IN p_email VARCHAR(100),
    IN p_phone VARCHAR(20),
    IN p_date_of_birth DATE,
    IN p_address VARCHAR(255),
    IN p_city VARCHAR(50),
    IN p_state VARCHAR(50),
    IN p_zip_code VARCHAR(10),
    IN p_initial_balance DECIMAL(15,2)
)
BEGIN
    DECLARE v_customer_id INT;
    DECLARE v_account_id INT;
    DECLARE v_account_number VARCHAR(20);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Insert new customer
    INSERT INTO Customers (first_name, last_name, email, phone, date_of_birth, address, city, state, zip_code)
    VALUES (p_first_name, p_last_name, p_email, p_phone, p_date_of_birth, p_address, p_city, p_state, p_zip_code);
    
    -- Get the new customer ID
    SET v_customer_id = LAST_INSERT_ID();
    
    -- Generate account number
    SET v_account_number = CONCAT('CHK', LPAD(v_customer_id, 3, '0'));
    
    -- Insert new account
    INSERT INTO Accounts (customer_id, account_number, account_type, balance)
    VALUES (v_customer_id, v_account_number, 'CHECKING', p_initial_balance);
    
    -- Get the new account ID
    SET v_account_id = LAST_INSERT_ID();
    
    -- Insert initial transaction
    INSERT INTO Transactions (account_id, transaction_type, amount, description, balance_after)
    VALUES (v_account_id, 'DEPOSIT', p_initial_balance, 'Initial account opening deposit', p_initial_balance);
    
    COMMIT;
    
    -- Return the new customer and account information
    SELECT 
        v_customer_id AS new_customer_id,
        v_account_id AS new_account_id,
        v_account_number AS new_account_number,
        p_initial_balance AS initial_balance;
        
END //

DELIMITER ;

-- =============================================
-- 7. DEPOSIT AND WITHDRAWAL FEATURES
-- =============================================

-- Create procedure for deposits
SELECT '=== CREATING DEPOSIT PROCEDURE ===' AS Query_Type;

DELIMITER //

CREATE PROCEDURE ProcessDeposit(
    IN p_account_id INT,
    IN p_amount DECIMAL(15,2),
    IN p_description TEXT
)
BEGIN
    DECLARE v_current_balance DECIMAL(15,2);
    DECLARE v_new_balance DECIMAL(15,2);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Get current balance
    SELECT balance INTO v_current_balance FROM Accounts WHERE account_id = p_account_id;
    
    -- Calculate new balance
    SET v_new_balance = v_current_balance + p_amount;
    
    -- Update account balance
    UPDATE Accounts SET balance = v_new_balance WHERE account_id = p_account_id;
    
    -- Insert transaction record
    INSERT INTO Transactions (account_id, transaction_type, amount, description, balance_after)
    VALUES (p_account_id, 'DEPOSIT', p_amount, p_description, v_new_balance);
    
    COMMIT;
    
    SELECT v_new_balance AS new_balance;
    
END //

DELIMITER ;

-- Create procedure for withdrawals
SELECT '=== CREATING WITHDRAWAL PROCEDURE ===' AS Query_Type;

DELIMITER //

CREATE PROCEDURE ProcessWithdrawal(
    IN p_account_id INT,
    IN p_amount DECIMAL(15,2),
    IN p_description TEXT
)
BEGIN
    DECLARE v_current_balance DECIMAL(15,2);
    DECLARE v_new_balance DECIMAL(15,2);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Get current balance
    SELECT balance INTO v_current_balance FROM Accounts WHERE account_id = p_account_id;
    
    -- Check if sufficient funds
    IF v_current_balance < p_amount THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient funds';
    END IF;
    
    -- Calculate new balance
    SET v_new_balance = v_current_balance - p_amount;
    
    -- Update account balance
    UPDATE Accounts SET balance = v_new_balance WHERE account_id = p_account_id;
    
    -- Insert transaction record
    INSERT INTO Transactions (account_id, transaction_type, amount, description, balance_after)
    VALUES (p_account_id, 'WITHDRAWAL', -p_amount, p_description, v_new_balance);
    
    COMMIT;
    
    SELECT v_new_balance AS new_balance;
    
END //

DELIMITER ;

-- =============================================
-- 8. TEST ALL FEATURES
-- =============================================

-- Test the AddNewCustomer procedure
SELECT '=== TESTING ADD NEW CUSTOMER ===' AS Query_Type;
CALL AddNewCustomer(
    'Michael', 'Johnson', 'michael.johnson@email.com', '555-0201', 
    '1990-06-15', '123 Bank St', 'Boston', 'MA', '02101', 
    1000.00
);

-- Test deposit procedure
SELECT '=== TESTING DEPOSIT ===' AS Query_Type;
CALL ProcessDeposit(1, 500.00, 'Salary deposit');

-- Test withdrawal procedure
SELECT '=== TESTING WITHDRAWAL ===' AS Query_Type;
CALL ProcessWithdrawal(1, 200.00, 'ATM withdrawal');

-- Test withdrawal with insufficient funds (should fail)
SELECT '=== TESTING INSUFFICIENT FUNDS ===' AS Query_Type;
CALL ProcessWithdrawal(1, 10000.00, 'Large withdrawal');

-- =============================================
-- 9. FINAL VERIFICATION QUERIES
-- =============================================

-- Show all customers with their accounts and balances
SELECT '=== FINAL CUSTOMER SUMMARY ===' AS Query_Type;
SELECT 
    c.customer_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    a.account_number,
    a.account_type,
    a.balance,
    COUNT(t.transaction_id) AS transaction_count
FROM Customers c
LEFT JOIN Accounts a ON c.customer_id = a.customer_id
LEFT JOIN Transactions t ON a.account_id = t.account_id
GROUP BY c.customer_id, a.account_id
ORDER BY c.last_name, a.account_number;

-- Show recent transactions
SELECT '=== RECENT TRANSACTIONS ===' AS Query_Type;
SELECT 
    t.transaction_id,
    a.account_number,
    t.transaction_type,
    t.amount,
    t.description,
    t.transaction_date,
    t.balance_after
FROM Transactions t
JOIN Accounts a ON t.account_id = a.account_id
ORDER BY t.transaction_date DESC
LIMIT 10;

-- Show active customers view
SELECT '=== ACTIVE CUSTOMERS SUMMARY ===' AS Query_Type;
SELECT * FROM ActiveCustomers ORDER BY total_balance DESC;

SELECT '=== ALL FEATURES COMPLETED SUCCESSFULLY ===' AS Status;