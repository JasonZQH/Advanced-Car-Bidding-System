#Drop table ADMIN;
CREATE TABLE ADMIN (
    AdminID INT(5),
    SSN VARCHAR(11),
    Name VARCHAR(50),
    Birthdate DATE,
    PRIMARY KEY (AdminID)
);

INSERT INTO ADMIN VALUES (12345,'333445555','John',NOW());
INSERT INTO ADMIN VALUES (12346,'987654321','Bob',NOW());
INSERT INTO ADMIN VALUES (12347,'888665555','Marry',NOW());

#Drop table USER;
CREATE TABLE USER
(UserID     INT(10),
Fname       VARCHAR(20),
Lname      	VARCHAR(20),
Gender 		VARCHAR(6),
Age			INT(3),
Phone		INT(11),
Email		VARCHAR(100),
Seller		BOOL,
Bidder		BOOL,
PrivacyPreference	VARCHAR(100),
AcitiveDate	DATE,
Street		VARCHAR(100),
City		VARCHAR(100),
State		VARCHAR(100),
Country		VARCHAR(100),
Zip			INT(15),
primary key (UserID)
);
INSERT INTO USER VALUES (00001,'James','Hardon','male',35,1234567890,'jh@qq.com',TRUE,FALSE,'PREFERENCE',NOW(),'J','H','CA','US',123);
INSERT INTO USER VALUES (00002,'Lebron','James','male',35,1234567890,'lj@qq.com',TRUE,FALSE,'PREFERENCE',NOW(),'L','J','CA','US',123);
INSERT INTO USER VALUES (00003,'Stephen','Curry','male',35,1234567890,'sc@qq.com',TRUE,FALSE,'PREFERENCE',NOW(),'S','C','CA','US',123);

