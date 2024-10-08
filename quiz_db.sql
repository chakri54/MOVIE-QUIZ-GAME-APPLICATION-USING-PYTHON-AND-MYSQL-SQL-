CREATE DATABASE quiz_game;

USE quiz_game;

CREATE TABLE quiz_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score FLOAT NOT NULL,
    gift VARCHAR(255),
    additional_cash FLOAT
);
