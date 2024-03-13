-- create the database hbtn_0d_usa and the
-- table states in that database on mysql server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select the database
USE hbtn_0d_usa;
-- create the table states in the db hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        name VARCHAR(256) NOT NULL
);
