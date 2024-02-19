-- a script that prepares a MYSQL server
-- db to use: hbnb_test_db, user: hbnb_test (in localhost)
-- password: hbnb_test_pwd
-- hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
-- hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail

-- create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create the user if it doesn't exist and set the password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the database performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to ensure the changes takes effect
FLUSH PRIVILEGES;
