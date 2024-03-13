-- create the database hbtn_0d_usa and the
-- table cities on mysql server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select the db to use
USE hbtn_0d_usa;
-- create the table cities
CREATE TABLE IF NOT EXISTS cities (
        id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        FOREIGN KEY(state_id) REFERENCES states(id)
);
