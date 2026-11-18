use adbms_practice;
create table Department(
DeptId int primary key,
DeptName varchar(50),
Location varchar(50));

describe department;

create table Employee(
EmpID int primary key,
EmpName varchar(50),
Salary decimal(10,2) check (Salary>0),
job varchar(30),
JoinDate Date,
DeptId int,
ManagerID int,
foreign key (DeptId) references Department(DeptId));

describe employee;

insert into Department values 
(10, 'IT', 'Pune'),
(20,'HR','Mumbai'),
(30,'Finance','Pune'),
(40,'Sales','Nashik');

select * from Department;

insert into Employee values 
(101,'Amit',50000,'Manager','2020-01-15',10,null),
(102, 'Sneha', 35000, 'Analyst', '2021-03-10', 10, 101),
(103, 'Rahul', 25000, 'Clerk', '2022-06-20', 20, 101),
(104, 'Priya', 45000, 'Analyst', '2019-11-05', 30, 101),
(105, 'Suresh', 30000, 'Clerk', '2023-02-12', 20, 103),
(106, 'Neha', 60000, 'Manager', '2018-07-25', 30, NULL),
(107, 'Kiran', 40000, 'Developer', '2022-09-01', 10, 101),
(108, 'Pooja', 28000, 'Developer', '2024-04-18', NULL, 102);

select * from Employee;

create table Student(
StudentID int primary key,
StudentName varchar(50),
Email varchar(50));

describe student;

alter table Employee
add constraint fk_e_d
foreign key (DeptId) references Department(DeptId);

select * from employee;

create table Project(
ProjectID int primary key,
ProjectName varchar(100),
Budget decimal(10,2));


describe Project;

alter table Employee
add Email varchar(50);

describe employee;

alter table employee
modify job varchar(50);

rename table EmployeeDetails to Employee;
show tables;

alter table employee
drop column Email;
describe employee;

create view EmployeeSalary as
select EmpId,EmpName,Salary
from employee;

select * from EmployeeSalary;

create or replace view EmployeeSalary as
select EmpId,EmpName,Salary
from Employee
where Salary >40000;

drop view EmployeeSalary;


create table NewEmployee(
EmpID int auto_increment primary key,
EmpName varchar(50));

describe newEmployee;

insert into Employee values
(109,'Rohan', 32000,'Developer','2020-05-10',10,101);

select * from employee;

insert into employee values
(110, 'Meera', 42000, 'Analyst', '2023-01-15', 30, 106),
(111, 'Vijay', 27000, 'Clerk', '2024-02-20', 20, 103);


update Employee
set Salary=40000
where EmpID=102;


update Employee
set Salary = Salary * 1.10
where empid>0;


update employee
set job='Analyst'
where empid=103;


delete from employee
where empid=108;


delete from employee
where deptid=20;


start transaction;

update employee
set salary=100000
where empid=101;

commit;
rollback;
savepoint sp1;

UPDATE Employee
SET Salary = 50000
WHERE EmpID = 104;

ROLLBACK TO SAVEPOINT sp1;

commit;


select * from employee;

select empname,salary
from employee;

select empname,salary
from employee
where salary>35000;


select *
from employee
where salary between 30000 and 50000;


select *
from employee
where deptid in (10,30);


select *
from employee
where empname like 'S%';


select * 
from employee
where empname like '%a';

select *
from employee
where empname like '%ha%';


select *
from employee
where deptid is null;


select *
from employee
order by salary asc;

select *
from employee
order by salary desc
limit 3;


select employee.empname,department.deptname
from employee
inner join department
on employee.deptid=department.deptid;


select distinct department.deptname
from employee
inner join department
on employee.deptid=department.deptid;


select employee.empname,department.deptname
from employee
left join department
on employee.deptid=department.deptid;

select employee.empname,department.deptname
from employee
right join department
on employee.deptid=department.deptid;

select employee.empname,department.deptname
from employee
left join department
on employee.deptid=department.deptid

union

select employee.empname,department.deptname
from employee
right join department
on employee.deptid=department.deptid;



describe student;

alter table student
modify studentName varchar(50) not null;


create table Users(
userid int primary key,
email varchar(50) unique);

describe users;


alter table employee
modify empname varchar(50) unique;

alter table employee
add constraint empnameuq 
unique(empname);

select * from employee;

alter table employee
modify empname varchar(50) not null;


create table Course(
courseid int primary key,
coursename varchar(100));


create table enrollment(
enrollmentid int primary key,
courseid int,
foreign key(courseid) references course(courseid));

describe course;
describe enrollment;


create table Staff(
staffid int primary key,
salary decimal(10,2) 
check (salary >0));

describe staff;

alter table employee
add constraint cksalary
check(salary >0);

describe employee;


create index idxname
on employee(empname);

drop index idxname
on employee;


select upper(empname) as UpperNames
from employee;

select lower(empname) as LowerName
from employee;


select empname,length(empname) as NameLength
from employee;

select empname, right(empname,3) as First_three
from employee;

select salary, right(empname,3) as First_three
from employee;


select trim(empname)
from employee;

select empname, replace(job,'Developer','Programer') as NewJob
from employee;


select empname,round(salary,-3) as RoundedSalary
from employee;


select 17%5 as Remainder;


select curdate() as Today;


select now() as CurDateTime;

select empname,year(joindate) as JoinYear
from employee;

select empname,month(joindate) as JoinMonth
from employee;

select Empname
from employee
where year(joindate)=2022;

select empname,timestampdiff(year,joindate,curdate()) as Experience
from employee;

select empname, year(curdate())-year(joindate)
from employee;

select year(now());

select date_format(joindate,'%d-%m-%y') DateFormat 
from employee;

select empname, ifnull(deptid,0) as DeptID
from employee;


select * from employee;

select count(*) as TotalEmployees
from employee;


select MIN(salary) as MinSalary
from employee;

select max(salary) as MaxSalary
from employee;

select sum(salary) TotalSalary
from employee;

select avg(salary) AvgSalary
from employee;


select deptid,count(*) as employeeCount
from employee
group by deptid;


select deptid,avg(salary) as avgsalary
from employee
group by deptid;


select deptid,avg(salary)
from employee
group by deptid
having avg(salary)>35000;

select * from department;

select count(employee.deptid) as itemployees
from employee
inner join department
on employee.deptid=department.deptid
where department.deptname='IT';


select distinct job
from employee;


select empname,salary
from employee
where salary>
(select avg(salary)
from employee);

select deptid,count(*) as employeecount
from employee
group by deptid
having count(*)>1;

