create database if not exists hdbms;
use hdbms;

drop table if exists patients;
drop table if exists hospital;
drop table if exists insurance;
drop table if exists doctor;
DROP TABLE IF EXISTS cities;

create table if not exists hospital
(
adrID int(10) unsigned NOT NULL,
cID int(10) unsigned NOT NULL,
street varchar(45) NOT NULL,
building varchar(45) NOT NULL,
primary key(adrID)
);

create table if not exists patients (
pID int (10) unsigned not null,
name varchar(45) not null,
gender varchar(10) not null,
phonenumber varchar(45) not null,
dob date not null,
id varchar(45) not null,
adrID int(10) unsigned NOT NULL,
primary key(pID),
constraint adrID foreign key(adrID) references hospital(adrID)
);


create table if not exists insurance(
pID int(10) unsigned not null,
company varchar(45) not null,
constraint pID foreign key(pID) references patients(pID)
);

create table if not exists doctor(
dID int(10) unsigned NOT NULL,
adrID int(10) unsigned NOT NULL,
name varchar(45) NOT NULL,
gender varchar(45) NOT NULL,
phonenumber varchar(45) NOT NULL,
dateOfBirth date NOT NULL,
KEY adrID2 (adrID),
PRIMARY KEY(adrID),
CONSTRAINT adrID2 FOREIGN KEY (adrID) REFERENCES hospital (adrID)
);

CREATE TABLE if not exists cities (
cID int(10) unsigned NOT NULL,
name varchar(45) NOT NULL,
PRIMARY KEY (cID)
);

select * from patients;
