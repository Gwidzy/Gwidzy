DROP DATABASE IF EXISTS chop_gui;
CREATE DATABASE chop_gui;
USE chop_gui;

CREATE TABLE Employee(
empID VARCHAR(40) PRIMARY KEY,
empRole VARCHAR(40),
empName VARCHAR(40),
empSurN VARCHAR(40),
empConNum VARCHAR(12),
empEmail VARCHAR(50),
empAdd VARCHAR(100),
empPayDetails VARCHAR(40),
empAvailable TINYINT
);

CREATE TABLE Clients(
clientID INT PRIMARY KEY,
clientName VARCHAR(40),
clientContact VARCHAR(40),
clientConNum VARCHAR(12),
clientEmail VARCHAR(45),
vatRegNo VARCHAR(20)
);

CREATE TABLE Project(
projID INT PRIMARY KEY,
projName VARCHAR(40),
projDesc VARCHAR(255),
projStartDate DATE,
projEndDate DATE,
projProofPay TINYINT,
projLocation VARCHAR(100),

clientName VARCHAR(40) REFERENCES Clients(clientName),
clientContact VARCHAR(40) REfERENCES Clients(clientContact),
vatRegNo VARCHAR(20) REfERENCES Clients(vatRegNo),
clientConNum VARCHAR(12) REfERENCES Clients(clientConNum),
clientEmail VARCHAR(45) REfERENCES Clients(clientEmail),

empName VARCHAR(40) REFERENCES Employee(empName)
);

CREATE TABLE Login(
loginID INT PRIMARY KEY,
userName VARCHAR(50),
pass VARCHAR(50)
);

INSERT INTO Employee(empID,empRole,empName,empSurN,empConNum,empAdd,empEmail,empPayDetails,empAvailable)
VALUES (1234567891011, 'Admin', 'Martin','Oliphant', '0794000966', '5 Gousblom Street, Blomtuin, Bellville, 7530','empEmail@gmail.com', 'Capitec Bank account number: 123456', 0
);

INSERT INTO Project(projID,projName,projDesc,projStartDate,projEndDate,projProofPay,projLocation,clientName,clientContact,vatRegNo,clientConNum,clientEmail,empName)
VALUES (148, 'Sundowns Stadium Restoration', 'Restoring Sundowns Stadium','2021-07-23', '2021-08-15', 1, '12 Sonop Road, Sundowns, Cape Town, 6942','Sundown Stadium','Piet','123456','0714549826','client@gmail.com','Martin'
);

INSERT INTO Clients(clientID,clientName,clientContact,clientConNum,vatRegNo,clientEmail)
VALUES (456, 'Sundown Stadium', 'Piet','0714549826', '123456', 'client@gmail.com'
);

INSERT INTO Login(loginID,userName,pass)
VALUES (069, 'Admin123', 'password123'
);

-- SELECT * FROM Employee;
-- SELECT * FROM Project;
-- SELECT * FROM Clients;
-- SELECT  FROM Login;