use studentinfodb;

create table studentinfo(
studentid int primary key,
studentname varchar(1000),
studentage int,
studentscore int);

create user 'studentdbuser'@'localhost' identified by 'studentdbuser';

-- Grant required privileges to the DB user

grant all privileges on studentdbinfo.* to 'studentdbuser'@'localhost';
