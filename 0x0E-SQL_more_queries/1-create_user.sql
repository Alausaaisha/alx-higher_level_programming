-- this script creates the MySQL server user user_0d_1
-- user_0d_1 has all privileges on the MySQL server
-- user_0d_1 password will be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, this script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
