create database Sem1practice;
use sem1practice;
show databases;

create table employee(
empid int primary key,
empname varchar(50),
city varchar(50),
department varchar(50));

describe employee;

create table investor(
invid int primary key,
invname varchar(50),
investment decimal(10,2),
empid int);

describe investor;

show tables;

insert into employee values
(1,'Amit','Pune','IT'),
(2,'Priya','Mumbai','HR'),
(3, 'Rahul', 'Nashik', 'Finance'),
(4, 'Sneha', 'Pune', 'IT'),
(5, 'Rohan', 'Nagpur', 'Sales');

select * from employee;

select department,count(*) as noofemp
from employee
group by department;

insert into investor values
(101,'Rajesh',50000,1),
(102, 'Neha', 75000, 2),
(103, 'Suresh', 60000, 3),
(104, 'Pooja', 90000, 4),
(105, 'Kiran', 40000, 5);

select * from investor;

create table Cource(
courceid int auto_increment primary key,
courcename varchar(50));

select * from cource;
describe cource;

insert into cource (courcename) values
('Database system');

create table employeebackup as
select * from employee;

select * from employeebackup;

alter table employee
add age int;

describe employee;

alter table employee
add salary decimal(10,2);

describe employee;

alter table employee
add constraint cksalary
check(salary>=10000);

alter table employee
add constraint ckage
check (age<=50);

show create table employee;

alter table investor
add age int;

alter table investor
modify invname text;

alter table investor
rename column empid to eid;

describe investor;

update employee
set city='Nagpur'
where empid=4;

select * from employee;

select *
from employee
where empid=4;

delete from investor
where invid=105;

select * from investor where invid=105;

alter table investor
drop column age;

alter table employee
drop check ckage;

show create table employee;

alter table employee
drop check cksalary;

