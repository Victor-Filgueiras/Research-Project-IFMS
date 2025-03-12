CREATE TABLE Servidores (
    fullName CHAR(100) NOT NULL,
    plateCode VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plateCode)
);

CREATE TABLE Estudantes (
    fullName CHAR(100) NOT NULL,
    plateCode VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plateCode)
);

CREATE TABLE Visitantes (
    fullName CHAR(100) NOT NULL,
    plateCode VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plateCode)
);
