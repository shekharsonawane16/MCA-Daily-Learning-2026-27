-- 1. Create a database named CompanyDB
CREATE DATABASE CompanyDB;

USE CompanyDB;

-- 2. Create Employees table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Salary DECIMAL(10,2),
    JoinDate DATE
);

-- 3. Create Departments table
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(100)
);

-- 4. Add Email column to Employees
ALTER TABLE Employees
ADD Email VARCHAR(100);

-- 5. Add dept_location column to Departments
ALTER TABLE Departments
ADD dept_location VARCHAR(100);

-- 6. Add NOT NULL constraint to the Phone column.
ALTER TABLE Employees
ADD Phone VARCHAR(15);

ALTER TABLE Employees
MODIFY Phone VARCHAR(15) NOT NULL;

-- 7. Change EmpName from VARCHAR(50) to VARCHAR(100)
ALTER TABLE Employees
MODIFY EmpName VARCHAR(100);

-- 8. Create a foreign key constraint between the two tables
ALTER TABLE Employees
ADD DeptID INT;

ALTER TABLE Employees
ADD CONSTRAINT FK_Employee_Department
FOREIGN KEY (DeptID)
REFERENCES Departments(DeptID);

-- 9. Drop the primary key constraint from Departments
ALTER TABLE Departments
DROP PRIMARY KEY;

-- 10. Rename EmpName to EmployeeName
ALTER TABLE Employees
RENAME COLUMN EmpName TO EmployeeName;

-- 11. Remove Phone column from Employees
ALTER TABLE Employees
DROP COLUMN Phone;

-- 12. Rename Employees table to EmployeeDetails
RENAME TABLE Employees TO EmployeeDetails;

-- 13. Delete the Departments table permanently
DROP TABLE Departments;
