CREATE TABLE Servidores (
    fullName CHAR(100) NOT NULL,
    plate VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plate)
);

CREATE TABLE Estudantes (
    fullName CHAR(100) NOT NULL,
    plate VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plate)
);

CREATE TABLE Visitantes (
    fullName CHAR(100) NOT NULL,
    plate VARCHAR(7) NOT NULL,
    PRIMARY KEY (fullName, plate)
);