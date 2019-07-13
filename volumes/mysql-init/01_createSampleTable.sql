create database if not exists sample;

create table if not exists sample.sample(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  num INT,
  text VARCHAR(100)
);

insert into sample.sample(num, text)
values
  (100, "サンプルデータ"),
  (200, "サンプルです"),
  (150, "ABC");
