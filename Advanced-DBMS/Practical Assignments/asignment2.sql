create database ADBMS_Practical2;
use ADBMS_Practical2;
create table Employee(
Emp_No int primary key,
E_name varchar(50),
E_address varchar(50),
E_ph_no varchar(15),
Dept_no int,
Dept_name varchar(50),
Job_id varchar(10),
Designation varchar(30),
Salary decimal(10,2),
Join_date date);

 show databases;
 show tables;
 describe Employee;
 
 insert into Employee
 (Emp_no,E_name,E_address,E_ph_no,Dept_no,Dept_name,Job_id,Designation,Salary,Join_Date)
 values
 (105,'Shekhar','Pune','9611131312',10,'IT','J01','ANALYST',50000,'2004-12-16'),
 (102,'Sagar','Mumbai','9143313131',20,'HR','J02','MANAGER',30000,'2003-01-03'),
 (103,'Dipak','Nashik','7454654564',30,'Sales','J03','CLERK',45000,'2002-08-02'),
 (104,'Hareram','Nashik','7454654564',40,'Sales','J04','CLERK',45000,'2002-09-02');

 
 select * from Employee;
 
 select Emp_No, E_name, Salary
 from Employee
 where upper(designation)='MANAGER';
 
 select * 
 from Employee
 where Salary >10000;
 
 select *
 from Employee
 where Join_date>='1982-01-01'
 order by Designation asc;
 
 select E_name,datediff(curdate(),Join_date)/365 as Experience, Salary/30 as Daily_Salary
 from Employee;
 
 
 select *
 from Employee
 where upper(Designation) in ('CLERK','ANALYST');
 
 select *
 from employee
 where Join_date in( '2004-12-16','2003-01-03');
 
 
 select *
 from Employee
 where Dept_no in(10,20);
 
 select *
 from employee
 where E_name like 'S%';
 
 select max(Salary) as Highest_Salary
 from employee;
 
 insert into Employee(
 Emp_no, E_name,E_address,E_ph_no,Dept_no,Dept_name,Job_id,Designation,Salary,Join_date)
 Values
 (105, 'Harsh', 'Pune', '9876543214', 30, 'Finance', 'J05', 'CLERK', 12000, '1982-06-15'),
(106, 'Priya', 'Mumbai', '9876543215', 10, 'IT', 'J06', 'ANALYST', 35000, '1983-03-10'),
(107, 'Sanjay', 'Pune', '9876543216', 20, 'HR', 'J07', 'PRESIDENT', 80000, '1979-07-20'),
(108, 'Hema', 'Nashik', '9876543217', 30, 'Finance', 'J08', 'MGR', 25000, '1984-09-05');

select E_name, left(E_name,5) as First_Five_Char
from employee
where E_name like 'H%';



select *
from Employee
where upper(Designation) not in ('PRSIDENT','MGR')
order by Salary asc;



select min(Salary) as Minimum_Salary,
max(Salary) as Maximum_Salary,
min(datediff(curdate(),Join_date)/365) as Min_Experience,
max(datediff(curdate(),Join_date)/365) as Max_Experience
from Employee;



select sum(Salary) as Total_Salary
from Employee;

select avg(Salary) as Avg_Salary
from employee
where upper(Dept_name)='IT';


select distinct Salary
from Employee;


drop database ADBMS_Practical2;