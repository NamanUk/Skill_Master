CREATE DATABASE skill_master;
USE skill_master;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    password VARCHAR(255) NOT NULL
);
