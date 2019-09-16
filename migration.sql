CREATE DATABASE IF NOT EXISTS cat;

USE cat;

# CREATE TABLE IF NOT EXISTS topic (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     description TEXT NOT NULL,
#     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     updated TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
# );

CREATE TABLE IF NOT EXISTS question (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL,
    difficulty FLOAT NOT NULL,
    discrimination FLOAT NOT NULL,
    pseudoguess FLOAT NOT NULL,
    choice_1 TEXT NOT NULL,
    choice_2 TEXT NOT NULL,
    choice_3 TEXT NOT NULL,
    choice_4 TEXT NOT NULL,
    choice_5 TEXT NOT NULL,
    choice_1_correct BOOLEAN NOT NULL,
    choice_2_correct BOOLEAN NOT NULL,
    choice_3_correct BOOLEAN NOT NULL,
    choice_4_correct BOOLEAN NOT NULL,
    choice_5_correct BOOLEAN NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);

# CREATE TABLE IF NOT EXISTS choice (
#     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     question_id INT NOT NULL,
#     description TEXT NOT NULL,
#     is_correct BOOLEAN NOT NULL,
#     created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     updated TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
# );

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(10) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS answer (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question_id INT NOT NULL,
    choice_id INT NOT NULL,
    is_correct BOOLEAN NOT NULL,
    question_order INT NOT NULL,
    theta FLOAT NOT NULL,
    probability_correct FLOAT NOT NULL,
    probability_wrong FLOAT NOT NULL,
    iif FLOAT NOT NULL,
    se FLOAT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
);
