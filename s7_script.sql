-- SQL

-- CREATE DATABASE comercio;

-- DROP DATABASE comercio;

USE comercio;

CREATE TABLE employees (
	emp_no int(11) NOT NULL AUTO_INCREMENT,
	first_name varchar(14) NOT NULL,
	last_name varchar(16) NOT NULL,
	gender enum('H','M') NOT NULL,
	birth_date date ,
	hire_date date ,
	PRIMARY KEY (emp_no)
);

DROP TABLE employees;



CREATE TABLE comercio.employees (
	emp_no int(11) NOT NULL AUTO_INCREMENT,
	first_name varchar(14) NOT NULL,
	last_name varchar(16) NOT NULL,
	gender enum('H','M') NOT NULL,
	birth_date date ,
	hire_date date ,
	PRIMARY KEY (emp_no)
);

DROP TABLE comercio.employees;


CREATE TABLE productos (
  id INT(6) NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(20) NOT NULL,
  descripcion VARCHAR(100) NOT NULL,
  precio INT(5) NOT NULL,
  PRIMARY KEY(id) 
);


USE comercio;

-- INSERSION DE REGISTROS

INSERT INTO employees (first_name, last_name, gender)VALUES ("Juan","Acosta","M")

INSERT INTO employees (first_name, last_name, gender)
VALUES 
	("Juan","Acosta","H"),
    ("Silvia","Garcia","M"),
    ("Maribel","Alegria","M");

-- SELECCCION DE REGISTROS
SELECT * FROM comercio.employees;


SELECT emp_no , last_name FROM comercio.employees;

SELECT emp_no as nro , last_name as Apellido FROM comercio.employees;

SELECT emp_no , last_name 
FROM comercio.employees
WHERE gender = "H";