create database if not exists hdbms;
use hdbms;

drop table if exists insurance;
drop table if exists doctor;
drop table if exists patients;
drop table if exists hospital;
DROP TABLE IF EXISTS cities;

CREATE TABLE if not exists cities (
cID int(10) unsigned not NULL auto_increment,
cname varchar(45) default NULL,
PRIMARY KEY (cID)
);

create table if not exists hospital
(

adrID int(10) unsigned not NULL auto_increment,
cID int(10) unsigned default NULL,
street varchar(45) default NULL,
building varchar(45) default NULL,
city varchar(45) default null,
primary key(adrID),
constraint cID foreign key(cID) references cities(cID) 
);

create table if not exists patients (
pID int (10) unsigned not null auto_increment,
adrID int(10) unsigned not null,
pname varchar(45) default null,
gender varchar(10) default null,
phonenumber varchar(45) default null,
dob varchar(45) default null,
primary key (pID),
constraint adrID foreign key(adrID) references hospital(adrID) 
);
       
create table if not exists insurance(
pID int(10) unsigned not null,
company varchar(45) default null,
constraint pID foreign key(pID) references patients(pID) 
);

create table if not exists doctor(
dID int(10) unsigned not NULL auto_increment,
adrID int(10) unsigned not NULL,
dname varchar(45) default NULL,
city varchar(45) default null,
gender varchar(45) default NULL,
phonenumber varchar(45) default NULL,
dateOfBirth varchar(45) default NULL,
PRIMARY KEY(dID)
);


insert into cities(cname)
values('Providence'),
('Cranston'),('Warwick');


insert into hospital(street, building,cid,city)
values('main st', '5A',1,'Cranston'), 
	('North st', '6B',2,'Providence'), 
	('South st', '7C',3,'Warwick');

insert into patients(pname,gender, phonenumber, dob,adrID)
values('Jack D', 'M', '1234567890', '05/24/1974',1), 
       ('Queen K', 'F', '12345670988', '04/07/1990',2), 
       ('Maria C', 'M', '1234567900', '10/15/1988',3);

insert into insurance(company,pID)
values('United Healthcare',1),
('McKennon Corp',2), 
('CVS Health',3);

insert into doctor(dname, gender, phonenumber, dateOfBirth,adrID,city)
values('Ricky Rubio','Male', '4016789342', '05/15/1969',1,'Warwick'), 
	('Lebron Howard', 'Male','4017595783', '12/30/1984',2,'Providence'),
        ('Kyle Kuzma', 'Male','4016721930', '07/26/1995',3,'Cranston');

/*SQL Testing Commands*/


select * from hospital;
select * from patients;
select * from cities;
select * from insurance;

update cities set cname = 'Kingston'  where cid = 3;
select * from cities;

alter table patients add homeaddress varchar(25);
select * from patients;
update patients set homeaddress = 'University Road' where pid = 1; 
update patients set homeaddress = '13 Health Ave' where pid = 2;
update patients set homeaddress = '81 Cranston St' where pid = 3;
select * from patients;

Create View patientcheckup as /* creating view of relevant patient infomation*/
    Select
        pname, gender, dob
    From
        patients P;
        
select * from patientcheckup;

SELECT * 
FROM doctor
NATURAL JOIN hospital;

SELECT pName FROM patients
left OUTER JOIN doctor
ON patients.adrID = doctor.adrID;

SELECT pName FROM patients
INNER JOIN doctor
ON patients.adrID = doctor.adrID;

SELECT pName FROM patients
left JOIN doctor
ON patients.adrID = doctor.adrID;

select pName from patients
where adrID in (select adrID from doctor where gender = 'Male');

create index insurance on patients (pname);
SHOW INDEX FROM insurance FROM hdbms;

CREATE USER admin@'localhost' IDENTIFIED BY 'test';  
GRANT ALL ON patients TO admin@'localhost';  
