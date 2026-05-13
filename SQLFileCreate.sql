Create DATABASE test2;
GO

USE test2;
GO

CREATE TABLE tbl_users(
	id INT IDENTITY(1,1) PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50),
	gender VARCHAR(20),
	age INT
);
GO