CREATE DATABASE ticketbuddy;
USE ticketbuddy;

CREATE TABLE user_details (
    username VARCHAR(50) PRIMARY KEY,
    phone_number VARCHAR(10),
    password VARCHAR(50)
);

CREATE TABLE user_seats (
    movie_name VARCHAR(50),
    seat_name VARCHAR(100),
    movie_date VARCHAR(20),
    movie_timings VARCHAR(20),
    username VARCHAR(50)
);