-- Make a file containing the SQL statements that create your entire database schema, named dbDDL.sql.  
-- This includes the tables with their constraints, view, indexes, triggers, and all other database objects if you have them.

-- To keep the project consistent, make sure you have at least 8 tables. Make sure you have the following database objects:
-- At least 1 trigger,
-- At least 1 function or procedure, and
-- At least 1 view.

CREATE TABLE Users (
    User_ID INT PRIMARY KEY,
    Email VARCHAR(255) UNIQUE,
    Phone_Number VARCHAR(20),
    Gender CHAR(1),
    Age INT,
    LastN VARCHAR(255),
    FirstN VARCHAR(255),
    Seller BOOLEAN,
    Bidder BOOLEAN,
    Privacy_Preference VARCHAR(255),
    Active_Date DATE,
    Street VARCHAR(255),
    State VARCHAR(255),
    ZIP VARCHAR(20),
    Country VARCHAR(255)
);

CREATE TABLE Auction (
    Auction_ID INT PRIMARY KEY,
    Auction_Status VARCHAR(255),
    Start_Time DATETIME,
    End_Time DATETIME,
    Start_Bid DECIMAL(10, 2),
    Reserve_Price DECIMAL(10, 2),
    Unsold BOOLEAN,
    Auction_Period INT,
    Attend_User_ID INT,
    Start_User_ID INT,
    FOREIGN KEY (Attend_User_ID) REFERENCES Users(User_ID),
    FOREIGN KEY (Start_User_ID) REFERENCES Users(User_ID)
);

CREATE TABLE Bid (
    Bid_ID INT PRIMARY KEY,
    User_ID INT,
    Auction_ID INT,
    Bid_Amount DECIMAL(10, 2),
    Bid_Time DATETIME,
    VIN VARCHAR(17),
    BIDWIN BOOLEAN,
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
    FOREIGN KEY (Auction_ID) REFERENCES Auction(Auction_ID)
);

CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY,
    Time DATETIME,
    Bidder INT,
    Seller INT,
    O_Price DECIMAL(10, 2),
    Payment_Method VARCHAR(255),
    VIN VARCHAR(17),
    Auction_ID INT,
    FOREIGN KEY (Bidder) REFERENCES Users(User_ID),
    FOREIGN KEY (Seller) REFERENCES Users(User_ID),
    FOREIGN KEY (Auction_ID) REFERENCES Auction(Auction_ID)
);

CREATE TABLE UserFeedback (
    Case_ID INT PRIMARY KEY,
    Seller_ID INT,
    FName VARCHAR(255),
    LName VARCHAR(255),
    Feedback VARCHAR(255),
    Category VARCHAR(255),
    ProvideFB_User_ID INT,
    FOREIGN KEY (ProvideFB_User_ID) REFERENCES Users(User_ID)
);

CREATE TABLE Payment (
    Payment_ID INT PRIMARY KEY,
    User_ID INT,
    Account VARCHAR(255),
    Payment_Method VARCHAR(255),
    Payment_Status VARCHAR(255),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

CREATE TABLE Car (
    VIN VARCHAR(17) PRIMARY KEY,
    Exterior_Color VARCHAR(255),
    Interior_Color VARCHAR(255),
    Make VARCHAR(255),
    Model VARCHAR(255),
    Fuel VARCHAR(255),
    Year INT,
    List_Time DATETIME,
    List_Price DECIMAL(10, 2),
    Current_Mileage INT
);
-- Subclasses of Car
CREATE TABLE Sedan (
    VIN VARCHAR(17) PRIMARY KEY,
    SeatNumber INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);
CREATE TABLE SUV (
    VIN VARCHAR(17) PRIMARY KEY,
    SeatNumber INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);
CREATE TABLE Convertible (
    VIN VARCHAR(17) PRIMARY KEY,
    CanopyMaterial VARCHAR(255),
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);
CREATE TABLE Electric (
    VIN VARCHAR(17) PRIMARY KEY,
    Electric_Range INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);
CREATE TABLE Hybrid (
    VIN VARCHAR(17) PRIMARY KEY,
    Fuel_Range INT,
    Electric_Range INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);
CREATE TABLE Truck (
    VIN VARCHAR(17) PRIMARY KEY,
    BoatLoad INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);

CREATE TABLE Report (
    Report_ID INT PRIMARY KEY,
    VIN VARCHAR(17),
    Detail_History TEXT,
    Owner_History TEXT,
    Title_History TEXT,
    Additional_History TEXT,
    History_Mileage INT,
    Owner_Count INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);

CREATE TABLE Shipping (
    Tracking_Number VARCHAR(255) PRIMARY KEY,
    Shipping_Method VARCHAR(255),
    Shipping_Status VARCHAR(255),
    Car_VIN VARCHAR(17),
    User_ID_Track INT,
    Approved_Payment_ID INT,
    FOREIGN KEY (Car_VIN) REFERENCES Car(VIN),
    FOREIGN KEY (User_ID_Track) REFERENCES Users(User_ID),
    FOREIGN KEY (Approved_Payment_ID) REFERENCES Payment(Payment_ID)
);

CREATE TABLE Admin (
    Admin_ID INT PRIMARY KEY,
    SSN VARCHAR(11) UNIQUE NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Birthdate DATE NOT NULL
);

CREATE TABLE Manage (
    Account_ID INT PRIMARY KEY,
    SSN VARCHAR(11),
    VIN VARCHAR(17),
    User_ID INT,
    FOREIGN KEY (SSN) REFERENCES Admin(SSN),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);

CREATE TABLE Transaction (
    Payment_ID INT,
    Order_ID INT,
    Transaction_ID INT PRIMARY KEY,
    Payment_Method VARCHAR(255),
    Time DATETIME,
    Transaction_Amount DECIMAL(10, 2),
    FOREIGN KEY (Payment_ID) REFERENCES Payment(Payment_ID),
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID)
);

-- Define a trigger that automatically updates the Auction_Status to 'CLOSED'
-- when an auction ends and there is a winning bid.
DELIMITER //
CREATE TRIGGER CloseAuction 
AFTER UPDATE ON Auction
FOR EACH ROW 
BEGIN
    IF NEW.End_Time <= CURRENT_TIMESTAMP() AND NEW.Unsold = FALSE THEN
        UPDATE Auction SET Auction_Status = 'CLOSED' WHERE Auction_ID = NEW.Auction_ID;
    END IF;
END;
//
DELIMITER ;

-- Add procedure
DELIMITER $$
CREATE PROCEDURE AddNewUser(
    IN p_Email VARCHAR(255),
    IN p_Phone_Number VARCHAR(20),
    IN p_Gender CHAR(1),
    IN p_Age INT,
    IN p_LastN VARCHAR(255),
    IN p_FirstN VARCHAR(255),
    IN p_Seller BOOLEAN,
    IN p_Bidder BOOLEAN,
    IN p_Privacy_Preference VARCHAR(255),
    IN p_Active_Date DATE,
    IN p_Street VARCHAR(255),
    IN p_State VARCHAR(255),
    IN p_ZIP VARCHAR(20),
    IN p_Country VARCHAR(255)
)
BEGIN
    INSERT INTO Users (Email, Phone_Number, Gender, Age, LastN, FirstN, Seller, Bidder, Privacy_Preference, Active_Date, Street, State, ZIP, Country)
    VALUES (p_Email, p_Phone_Number, p_Gender, p_Age, p_LastN, p_FirstN, p_Seller, p_Bidder, p_Privacy_Preference, p_Active_Date, p_Street, p_State, p_ZIP, p_Country);
END$$
DELIMITER ;


-- Create a view that shows the winning bids for auctions
CREATE VIEW WinningBids AS
SELECT B.Auction_ID, B.Bid_Amount, B.Bid_Time, B.VIN
FROM Bid B
WHERE B.BIDWIN = TRUE;
