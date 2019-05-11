/* 1. Create all the tables given in following schema. Define required constraints on given tables. Define triggered actions that will be attached to each foreign key constraint. */
Create Table BORROWER (Card_no CHAR(10) NOT NULL, Name varchar(50),Address varchar(255),Phone int, constraint Bpk PRIMARY KEY(Card_no));
Create Table LIBRARY_BRANCH (Branch_id CHAR(10) NOT NULL, Branch_Name varchar(50),Address varchar(255), constraint BRpk PRIMARY KEY(Branch_id));
Create Table PUBLISHER (Name varchar(50) NOT NULL,Address varchar(255),Phone int, constraint Npk PRIMARY KEY(Name));
Create Table BOOK (Book_id VARCHAR2(13) NOT NULL, Title varchar(255),Publisher_name varchar(255),Phone int, constraint BOpk PRIMARY KEY(Book_id),constraint Bfk FOREIGN KEY(Publisher_name) REFERENCES PUBLISHER(NAME) ON DELETE CASCADE);
Create Table BOOK_AUTHORS (Book_id VARCHAR2(13) NOT NULL, Author_Name varchar(255), constraint Ipk PRIMARY KEY(Book_id,Author_Name),constraint BOfk FOREIGN KEY(Book_id) REFERENCES BOOK(Book_id) ON DELETE CASCADE);

Create Table BOOK_COPIES (Book_id VARCHAR2(13) NOT NULL, Branch_id CHAR(10) NOT NULL,No_Of_Copies NUMBER DEFAULT 0, constraint BOCpk PRIMARY KEY(Book_id,branch_id),
constraint BOCfk FOREIGN KEY(Book_id) REFERENCES BOOK(Book_id) ON DELETE CASCADE,
constraint BOBfk FOREIGN KEY(Branch_id) REFERENCES LIBRARY_BRANCH(Branch_id) ON DELETE CASCADE);

Create Table BOOK_LOANS (Book_id VARCHAR2(13) NOT NULL, Branch_id CHAR(10) NOT NULL,Card_no CHAR(10) NOT NULL,Date_out date,Due_date date,Return_date date DEFAULT NULL ,constraint BOLpk PRIMARY KEY(Book_id,branch_id,Card_no),
constraint BOLfk FOREIGN KEY(Book_id) REFERENCES BOOK(Book_id) ON DELETE CASCADE,
constraint BOBLfk FOREIGN KEY(Branch_id) REFERENCES LIBRARY_BRANCH(Branch_id) ON DELETE CASCADE,
constraint BOBCfk FOREIGN KEY(Card_no) REFERENCES BORROWER(Card_no) ON DELETE CASCADE);



-- Q1)
/*a) For each department whose average employee salary is more than $30,000, retrieve the department name and the number of employees working for that department. */
Select DEPARTMENT.DNAME AS DEPARTMENT_NAME, Count(*) AS EMPLOYEE_NUM from EMPLOYEE,DEPARTMENT WHERE DEPARTMENT.DNO=EMPLOYEE.DNO Group By DEPARTMENT.DNAME Having AVG(SALARY)>30000;

/*b) Same as a, except output the number of male employees instead of the number of employees. */
Select DEPARTMENT.DNAME AS DEPARTMENT_NAME, Count(*) AS MALE_EMPLOYEES from EMPLOYEE,DEPARTMENT WHERE DEPARTMENT.DNO=EMPLOYEE.DNO AND EMPLOYEE.GENDER='M' Group By DEPARTMENT.DNAME Having AVG(SALARY)>30000;

/*c) Retrieve the names of all employees who work in the department that has the employee with the highest salary among all employees. */
SELECT FNAME||' '||LNAME AS EMPLOYEE FROM EMPLOYEE where DNO =(Select DNO from EMPLOYEE where SALARY=(Select MAX(SALARY) from EMPLOYEE));

/*d) Retrieve the names of employees who make at least $10,000 more than the employee who is paid the least in the company. */
SELECT FNAME||' '||LNAME AS EMPLOYEE FROM EMPLOYEE WHERE SALARY>=(select min(salary)+10000 from EMPLOYEE);

/*e) Retrieve the names of employees who is making least in their departments and have more than one dependent. (solve using correlated nested queries) */
select FNAME||' '||LNAME AS EMPLOYEE from EMPLOYEE where (SALARY,DNO) in (select min(salary),dno from EMPLOYEE group by dno) and SSN in (SELECT ESSN from DEPENDENT Group by ESSN Having count(*)>1) ;


-- Q2)

/*a) A view that has the department name, manager name and manager salary for every department.*/
CREATE view MANAGER_INFO AS SELECT d.DNAME AS DEPARTMENT_NAME, e.FNAME||' '||e.LNAME AS MANAGER, e.SALARY from EMPLOYEE e,DEPARTMENT d where e.SSN=d.MGRSSN;


/*b) A view that has the department name, its manager's name, number of employees working in that department, and the number of projects controlled by that department (for each department). */
CREATE view DEPARTMENT_INFO AS SELECT d.DNAME AS DEPARTMENT, e.FNAME||' '||e.LNAME AS MANAGER,(SELECT  Count(*) from EMPLOYEE s where s.DNO=d.DNO  group by s.DNO) NO_OF_EMP,(SELECT Count(*) from Project p where p.DNO=d.dno  group by p.DNO) No_of_proj from EMPLOYEE e,DEPARTMENT d where e.SSN=d.MGRSSN;


/*c)A view that has the project name, controlling department name, number of employees working on the project, and the total hours per week they work on the project (for each project).*/
CREATE VIEW PROJECT_INFO1 AS SELECT p.PNAME AS PROJECT,d.DNAME AS DEPARTMENT,Count(*)NO_OF_EMP,(SELECT SUM(wo.HOURS) from WORKS_ON wo where wo.pno=p.pno group by wo.pno) TOTAL_HOURS from PROJECT p, DEPARTMENT d,WORKS_ON w,Employee e where p.DNO=d.DNO and w.PNO=p.pno and e.ssn=w.ssn group by p.PNO,p.PNAME,d.DNAME;


/*d)A view that has the project name, controlling department name, number of employees, and total hours worked per week on the project for each project with more than one employee working on it.*/
CREATE VIEW PROJECT_INFO2 AS SELECT p.PNAME AS PROJECT,d.DNAME AS DEPARTMENT,Count(*)NO_OF_EMP,(SELECT SUM(wo.HOURS) from WORKS_ON wo where wo.pno=p.pno group by wo.pno) TOTAL_HOURS from PROJECT p, DEPARTMENT d,WORKS_ON w,Employee e where p.DNO=d.DNO and w.PNO=p.pno and e.ssn=w.ssn group by p.PNO,p.PNAME,d.DNAME having COUNT(*)>1;


/*e)A view that has the employee name, employee salary, department that the employee works in, department manager name, manager salary, and average salary for the department. (Hint: Find average salary for the department by using correlated nested query. You can have correlated nested queries also in SELECT clause.)*/
CREATE VIEW EMPLOYEE_INFO AS SELECT e.FNAME||' '||e.LNAME AS EMPLOYEE, e.SALARY, d.DNAME AS DEPARTMENT,(SELECT p.FNAME||' '||p.LNAME from EMPLOYEE p where p.ssn=d.MGRSSN) MANAGER,(SELECT p.SALARY from EMPLOYEE p where p.ssn=d.MGRSSN) MGR_SALARY,(SELECT AVG(s.SALARY) from EMPLOYEE s where d.DNO=s.DNO group by s.DNO) AVG_SAL from EMPLOYEE e,DEPARTMENT d where d.DNO=e.DNO; 

