create database if not exists sample;

create table if not exists sample.sample(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  num INT,
  text VARCHAR(100)
);
