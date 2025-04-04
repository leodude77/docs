
create database if not exists practice_commands;
use practice_commands;

-- Create table statement
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    quantity INT,
    description TEXT
);

-- Insert statements with 20 records
INSERT INTO products (product_id, product_name, category, price, quantity, description) VALUES
(1, 'Apple iPhone 15', 'Electronics', 999.99, 50, 'Latest model with advanced features'),
(2, 'Samsung Galaxy S23', 'Electronics', 849.99, 40, 'Flagship smartphone with great camera'),
(3, 'Sony WH-1000XM5', 'Audio', 349.99, 30, 'Noise-canceling headphones with premium sound'),
(4, 'Nike Air Max 2023', 'Footwear', 139.99, 100, 'Comfortable sneakers for all-day wear'),
(5, 'Dell XPS 13', 'Computers', 1199.99, 25, 'Ultraportable laptop with high-end performance'),
(6, 'Bose SoundLink Flex', 'Audio', 129.99, 60, 'Portable Bluetooth speaker with great sound'),
(7, 'GoPro HERO10', 'Cameras', 399.99, 75, 'Action camera with 5.3K video recording'),
(8, 'Apple Watch Series 8', 'Wearables', 399.99, 80, 'Smartwatch with health and fitness features'),
(9, 'Canon EOS Rebel T8i', 'Cameras', 849.99, 20, 'DSLR camera for beginners with a good lens kit'),
(10, 'LG OLED TV 55"', 'Electronics', 1399.99, 10, '55-inch 4K OLED television with stunning colors'),
(11, 'Microsoft Surface Pro 9', 'Computers', 1099.99, 15, '2-in-1 laptop and tablet with powerful specs'),
(12, 'Harman Kardon Onyx Studio 7', 'Audio', 299.99, 50, 'Wireless speaker with premium design and sound'),
(13, 'Kindle Paperwhite', 'Books', 129.99, 120, 'Waterproof e-reader with built-in light'),
(14, 'Sony PlayStation 5', 'Gaming', 499.99, 30, 'Next-gen gaming console with powerful hardware'),
(15, 'Samsung 980 Pro SSD 1TB', 'Storage', 179.99, 150, 'High-speed solid-state drive for gaming and productivity'),
(16, 'Fitbit Charge 5', 'Wearables', 149.99, 200, 'Fitness tracker with built-in GPS and heart rate monitor'),
(17, 'JBL Flip 6', 'Audio', 119.99, 85, 'Compact portable Bluetooth speaker'),
(18, 'Apple MacBook Pro 14"', 'Computers', 1999.99, 40, 'High-performance laptop for professionals'),
(19, 'Razer Kraken V3', 'Gaming', 129.99, 90, 'Gaming headset with surround sound and RGB lighting'),
(20, 'Nikon D7500 DSLR', 'Cameras', 1199.99, 35, 'DSLR camera with excellent autofocus and 4K video');

-- Create table statement for customers_transactions
CREATE TABLE customers_transactions (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    transaction_date TIMESTAMP,
    quantity INT,
    total_amount DECIMAL(10, 2),
    payment_method VARCHAR(50),
    shipping_address VARCHAR(255),
    status VARCHAR(50),
    discount DECIMAL(5, 2)
);
--FOREIGN KEY (product_id) REFERENCES products(product_id)

-- Insert 50 records into the customers_transactions table
INSERT INTO customers_transactions (transaction_id, customer_id, product_id, transaction_date, quantity, total_amount, payment_method, shipping_address, status, discount) VALUES
(1, 101, 1, '2025-03-01 10:00:00', 2, 1999.98, 'Credit Card', '123 Elm St, Springfield', 'Completed', 10.00),
(2, 102, 3, '2025-03-02 11:15:00', 1, 349.99, 'PayPal', '456 Oak St, Springfield', 'Completed', 5.00),
(3, 103, 4, '2025-03-03 12:30:00', 1, 139.99, 'Debit Card', '789 Pine St, Shelbyville', 'Pending', 0.00),
(4, 104, 6, '2025-03-04 13:45:00', 3, 389.97, 'Credit Card', '321 Maple St, Springfield', 'Completed', 15.00),
(5, 105, 2, '2025-03-05 14:00:00', 2, 1699.98, 'Debit Card', '654 Birch St, Capital City', 'Shipped', 10.00),
(6, 106, 5, '2025-03-06 15:30:00', 1, 1199.99, 'Credit Card', '987 Cedar St, Shelbyville', 'Completed', 20.00),
(7, 107, 7, '2025-03-07 16:10:00', 1, 399.99, 'PayPal', '159 Walnut St, Springfield', 'Completed', 0.00),
(8, 108, 8, '2025-03-08 17:25:00', 1, 399.99, 'Credit Card', '753 Oak St, Springfield', 'Shipped', 5.00),
(9, 109, 9, '2025-03-09 18:40:00', 1, 849.99, 'Debit Card', '258 Pine St, Springfield', 'Completed', 0.00),
(10, 110, 10, '2025-03-10 19:55:00', 2, 2799.98, 'Credit Card', '432 Elm St, Capital City', 'Completed', 10.00),
(11, 101, 11, '2025-03-11 10:00:00', 3, 449.97, 'PayPal', '123 Elm St, Springfield', 'Shipped', 5.00),
(12, 102, 12, '2025-03-12 11:15:00', 1, 1299.99, 'Credit Card', '456 Oak St, Springfield', 'Completed', 0.00),
(13, 103, 13, '2025-03-13 12:30:00', 1, 1999.99, 'Debit Card', '789 Pine St, Shelbyville', 'Pending', 20.00),
(14, 104, 14, '2025-03-14 13:45:00', 2, 1399.98, 'Credit Card', '321 Maple St, Springfield', 'Shipped', 10.00),
(15, 105, 15, '2025-03-15 14:00:00', 1, 399.99, 'Debit Card', '654 Birch St, Capital City', 'Completed', 0.00),
(16, 106, 16, '2025-03-16 15:30:00', 1, 1199.99, 'PayPal', '987 Cedar St, Shelbyville', 'Completed', 5.00),
(17, 107, 17, '2025-03-17 16:10:00', 3, 249.99, 'Credit Card', '159 Walnut St, Springfield', 'Shipped', 10.00),
(18, 108, 18, '2025-03-18 17:25:00', 2, 1399.99, 'Debit Card', '753 Oak St, Springfield', 'Completed', 15.00),
(19, 109, 19, '2025-03-19 18:40:00', 1, 849.99, 'PayPal', '258 Pine St, Springfield', 'Shipped', 0.00),
(20, 110, 20, '2025-03-20 19:55:00', 4, 199.99, 'Credit Card', '432 Elm St, Capital City', 'Completed', 5.00),
(21, 101, 3, '2025-03-21 10:00:00', 1, 349.99, 'Debit Card', '123 Elm St, Springfield', 'Completed', 0.00),
(22, 102, 5, '2025-03-22 11:15:00', 1, 1199.99, 'Credit Card', '456 Oak St, Springfield', 'Pending', 10.00),
(23, 103, 7, '2025-03-23 12:30:00', 1, 399.99, 'PayPal', '789 Pine St, Shelbyville', 'Shipped', 0.00),
(24, 104, 10, '2025-03-24 13:45:00', 2, 2799.98, 'Credit Card', '321 Maple St, Springfield', 'Completed', 5.00),
(25, 105, 8, '2025-03-25 14:00:00', 1, 399.99, 'Debit Card', '654 Birch St, Capital City', 'Completed', 5.00),
(26, 106, 6, '2025-03-26 15:30:00', 2, 799.98, 'PayPal', '987 Cedar St, Shelbyville', 'Shipped', 10.00),
(27, 107, 2, '2025-03-27 16:10:00', 3, 849.99, 'Credit Card', '159 Walnut St, Springfield', 'Completed', 0.00),
(28, 108, 4, '2025-03-28 17:25:00', 1, 139.99, 'Debit Card', '753 Oak St, Springfield', 'Pending', 5.00),
(29, 109, 9, '2025-03-29 18:40:00', 1, 849.99, 'PayPal', '258 Pine St, Springfield', 'Shipped', 0.00),
(30, 110, 11, '2025-03-30 19:55:00', 3, 449.97, 'Credit Card', '432 Elm St, Capital City', 'Completed', 10.00),
(31, 101, 12, '2025-03-31 10:00:00', 1, 1299.99, 'Debit Card', '123 Elm St, Springfield', 'Shipped', 5.00),
(32, 102, 14, '2025-04-01 11:15:00', 2, 1399.98, 'PayPal', '456 Oak St, Springfield', 'Pending', 0.00),
(33, 103, 16, '2025-04-02 12:30:00', 1, 1199.99, 'Credit Card', '789 Pine St, Shelbyville', 'Completed', 0.00),
(34, 104, 18, '2025-04-03 13:45:00', 2, 1399.98, 'Debit Card', '321 Maple St, Springfield', 'Shipped', 10.00),
(35, 105, 5, '2025-04-04 14:00:00', 1, 1199.99, 'PayPal', '654 Birch St, Capital City', 'Shipped', 20.00),
(36, 106, 19, '2025-04-05 15:30:00', 3, 449.97, 'Credit Card', '987 Cedar St, Shelbyville', 'Shipped', 5.00),
(37, 107, 20, '2025-04-06 16:10:00', 1, 199.99, 'Debit Card', '159 Walnut St, Springfield', 'Completed', 0.00),
(38, 108, 4, '2025-04-07 17:25:00', 1, 139.99, 'PayPal', '753 Oak St, Springfield', 'Completed', 10.00),
(39, 109, 3, '2025-04-08 18:40:00', 2, 699.98, 'Credit Card', '258 Pine St, Springfield', 'Shipped', 0.00),
(40, 110, 6, '2025-04-09 19:55:00', 1, 399.99, 'Debit Card', '432 Elm St, Capital City', 'Completed', 5.00),
(41, 101, 9, '2025-04-10 10:00:00', 1, 849.99, 'PayPal', '123 Elm St, Springfield', 'Shipped', 0.00),
(42, 102, 7, '2025-04-11 11:15:00', 1, 399.99, 'Debit Card', '456 Oak St, Springfield', 'Completed', 10.00),
(43, 103, 13, '2025-04-12 12:30:00', 2, 799.98, 'Credit Card', '789 Pine St, Shelbyville', 'Completed', 0.00),
(44, 104, 17, '2025-04-13 13:45:00', 1, 249.99, 'PayPal', '321 Maple St, Springfield', 'Shipped', 10.00),
(45, 105, 14, '2025-04-14 14:00:00', 1, 1399.99, 'Credit Card', '654 Birch St, Capital City', 'Pending', 5.00),
(46, 106, 8, '2025-04-15 15:30:00', 2, 799.98, 'PayPal', '987 Cedar St, Shelbyville', 'Completed', 10.00),
(47, 107, 19, '2025-04-16 16:10:00', 1, 849.99, 'Credit Card', '159 Walnut St, Springfield', 'Completed', 5.00),
(48, 108, 2, '2025-04-17 17:25:00', 1, 349.99, 'Debit Card', '753 Oak St, Springfield', 'Shipped', 10.00),
(49, 109, 15, '2025-04-18 18:40:00', 3, 449.97, 'PayPal', '258 Pine St, Springfield', 'Completed', 0.00),
(50, 110, 11, '2025-04-19 19:55:00', 2, 2799.98, 'Credit Card', '432 Elm St, Capital City', 'Shipped', 10.00);

# ==========================================================================================================================
# SQOOP IMPORT
# ==========================================================================================================================

sqoop import --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera\
 --table products --m 4 --delete-target-dir --target-dir /user/cloudera/indir

# Controlling imports
# Using WHERE
sqoop import --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera\
 --table products --m 1 --delete-target-dir --target-dir /user/cloudera/products_less_than_200 --where "price<200"

# Query import - Note REQUIRES WHERE $CONDITIONS
sqoop import --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera\
 --m 1 --delete-target-dir --target-dir /user/cloudera/products_less_than_200 --query "select * from products where price<200 AND \$CONDITIONS"

# Eval in sqoop -- to check query output is as expected
sqoop eval --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera\
 --query "select * from products p inner join customers_transactions ct on p.product_id = ct.product_id"


# -------------------------------------------------------------------------------------------------------------------------
# Inserting records for incremental import

INSERT INTO customers_transactions (transaction_id, customer_id, product_id, transaction_date, quantity, total_amount, payment_method, shipping_address, status, discount) VALUES
(51, 111, 3, '2025-04-20 10:00:00', 1, 349.99, 'Credit Card', '321 Birch St, Springfield', 'Completed', 10.00),
(52, 112, 6, '2025-04-21 11:15:00', 2, 799.98, 'Debit Card', '432 Oak St, Springfield', 'Shipped', 5.00),
(53, 113, 8, '2025-04-22 12:30:00', 1, 399.99, 'PayPal', '543 Pine St, Capital City', 'Shipped', 0.00),
(54, 114, 7, '2025-04-23 13:45:00', 3, 449.97, 'Credit Card', '654 Cedar St, Shelbyville', 'Completed', 0.00),
(55, 115, 2, '2025-04-24 14:00:00', 2, 1399.98, 'Debit Card', '765 Oak St, Springfield', 'Pending', 10.00),
(56, 116, 10, '2025-04-25 15:30:00', 1, 199.99, 'PayPal', '876 Birch St, Capital City', 'Shipped', 5.00),
(57, 117, 4, '2025-04-26 16:10:00', 2, 799.98, 'Credit Card', '987 Pine St, Springfield', 'Completed', 20.00),
(58, 118, 5, '2025-04-27 17:25:00', 1, 1199.99, 'Debit Card', '654 Elm St, Shelbyville', 'Shipped', 15.00),
(59, 119, 13, '2025-04-28 18:40:00', 1, 1299.99, 'Credit Card', '543 Oak St, Springfield', 'Completed', 5.00),
(60, 120, 15, '2025-04-29 19:55:00', 2, 1399.98, 'PayPal', '321 Walnut St, Capital City', 'Shipped', 10.00),
(61, 111, 11, '2025-04-30 10:00:00', 3, 449.97, 'Debit Card', '432 Elm St, Springfield', 'Completed', 0.00),
(62, 112, 12, '2025-05-01 11:15:00', 2, 1399.98, 'Credit Card', '765 Cedar St, Capital City', 'Completed', 10.00),
(63, 113, 9, '2025-05-02 12:30:00', 1, 849.99, 'PayPal', '543 Birch St, Springfield', 'Shipped', 0.00),
(64, 114, 20, '2025-05-03 13:45:00', 1, 399.99, 'Debit Card', '654 Oak St, Shelbyville', 'Pending', 5.00),
(65, 115, 16, '2025-05-04 14:00:00', 3, 449.97, 'Credit Card', '765 Pine St, Springfield', 'Completed', 15.00),
(66, 116, 17, '2025-05-05 15:30:00', 1, 249.99, 'PayPal', '876 Cedar St, Springfield', 'Shipped', 10.00),
(67, 117, 18, '2025-05-06 16:10:00', 2, 1399.98, 'Debit Card', '987 Oak St, Capital City', 'Completed', 0.00),
(68, 118, 14, '2025-05-07 17:25:00', 1, 1399.99, 'Credit Card', '654 Pine St, Shelbyville', 'Shipped', 20.00),
(69, 119, 19, '2025-05-08 18:40:00', 1, 849.99, 'PayPal', '543 Maple St, Springfield', 'Shipped', 5.00),
(70, 120, 3, '2025-05-09 19:55:00', 2, 699.98, 'Debit Card', '321 Oak St, Capital City', 'Completed', 0.00);

DELETE FROM customers_transactions WHERE transaction_id IN (51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70);

# -------------------------------------------------------------------------------------------------------------------------

# Incremental import
# Note => --append and --delete-target-dir can not be used together.
sqoop import --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera --m 1\
 --target-dir /user/cloudera/incremental --table customers_transactions\
 --check-column transaction_id --incremental append --last-value 25

# Create sqoop job
sqoop job --create inc_import -- import --connect jdbc:mysql://localhost/practice_commands --username root --password cloudera --m 1\
 --target-dir /user/cloudera/incremental_data --table customers_transactions\
 --check-column transaction_id --incremental append --last-value 50

# Using password-file, else have provide password when using show and exec
# echo -n cloudera >> pfile
sqoop job --create inc_import_v2 -- import --connect jdbc:mysql://localhost/practice_commands --username root --password-file file:///home/cloudera/passfile --m 1\
 --target-dir /user/cloudera/products_less_than_200 --table customers_transactions\
 --check-column transaction_id --incremental append --last-value 50

# Sqoop export all tables - if warehouse-dir is not provided, it stores it under /user/${user_id} directory
sqoop import-all-tables --connect jdbc:mysql://localhost/practice_commands --username root --password-file file:///home/cloudera/pfile \
 --warehouse-dir /user/cloudera/import-all-except-cust-trans --exclude-tables "customers_transactions" --m 1

# --------------------------------------------------------------------------------------------------------------
delete from customers_transactions where transaction_id IN (45,46,47,48,49,50);

INSERT INTO customers_transactions (transaction_id, customer_id, product_id, transaction_date, quantity, total_amount, payment_method, shipping_address, status, discount) VALUES
(45, 105, 14, '2025-04-22 14:00:00', 1, 1399.99, 'Updated record', '654 Birch St, Capital City', 'Pending', 5.00),
(46, 106, 8, '2025-04-22 15:30:00', 2, 799.98, 'Updated record', '987 Cedar St, Shelbyville', 'Completed', 10.00),
(47, 107, 19, '2025-04-22 16:10:00', 1, 849.99, 'Updated record', '159 Walnut St, Springfield', 'Completed', 5.00),
(48, 108, 2, '2025-04-22 17:25:00', 1, 349.99, 'Updated record', '753 Oak St, Springfield', 'Shipped', 10.00),
(49, 109, 15, '2025-04-22 18:40:00', 3, 449.97, 'Updated record', '258 Pine St, Springfield', 'Completed', 0.00),
(50, 110, 11, '2025-04-22 19:55:00', 2, 2799.98, 'Updated record', '432 Elm St, Capital City', 'Shipped', 10.00);

sqoop import --connect jdbc:mysql://localhost/practice_commands --username root --password-file file:///home/cloudera/pfile --m 1\
 --target-dir /user/cloudera/cust_50 --table customers_transactions --incremental lastmodified \
 --check-column transaction_date --last-value '2025-04-20' --merge-key transaction_id
