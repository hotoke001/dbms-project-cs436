/*SQL Testing Commands*/


select * from hospital;
select * from patients;
select * from cities;
select * from insurance;

update cities set cname = 'Kingston'  where cid = 3;
select * from cities;

select * from patients natural join doctor;
alter table patients add homeaddress varchar(25);
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
