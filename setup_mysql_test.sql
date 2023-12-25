-- Write a script that prepares a MySQL server for the project:

-- A database hbnb_test_db
-- A new user hbnb_test (in localhost)
-- The password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test should have all privileges on the database -- hbnb_test_db (and only this database)
-- hbnb_test should have SELECT privilege on the database performance_schema (and only this database)


-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update the user hbnb_test with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the database hbnb_test_db to the user hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database performance_schema to the user hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
