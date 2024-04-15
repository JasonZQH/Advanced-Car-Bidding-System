-- Make a file containing INSERT statements which populate the table created in Step 9, named dbDML.sql.  
-- This script will contain SQL commands to fill data in your data.  Each table should have around 7 ~ 10 sample data. 
-- If needed, other DML statement, such UPDATE, and DELETE can be included here

-- INSERT INTO Users (User_ID, Email, Phone_Number, Gender, Age, LastN, FirstN, Seller, Bidder, Active_Date, Street, State, ZIP, Country)
-- VALUES
-- (12345678, 'user1@gmail.com', '123-456-7890', 'M', 25, 'Doe', 'John', TRUE, FALSE,  '2024-03-11', '123 Main St', 'CA', '90001', 'USA'),
-- (23456789, 'user2@outlook.com', '234-567-8901', 'F', 30, 'Smith', 'Jane', FALSE, TRUE, '2024-03-10', '456 Elm St', 'NY', '10001', 'USA'),
-- (34567890, 'user3@gmail.com', '345-678-9012', 'M', 28, 'Johnson', 'Mike', TRUE, TRUE,  '2024-03-09', '789 Maple Ave', 'TX', '75001', 'USA'),
-- (45678901, 'user4@outlook.com', '456-789-0123', 'F', 22, 'Williams', 'Emily', FALSE, FALSE, '2024-03-08', '321 Oak St', 'FL', '33101', 'USA'),
-- (56789012, 'user5@gmail.com', '567-890-1234', 'M', 35, 'Brown', 'Chris', TRUE, FALSE,  '2024-03-07', '654 Pine St', 'IL', '60601', 'USA'),
-- (67890123, 'user6@outlook.com', '678-901-2345', 'F', 27, 'Jones', 'Anna', FALSE, TRUE,  '2024-03-06', '987 Cedar St', 'PA', '19101', 'USA'),
-- (78901234, 'user7@gmail.com', '789-012-3456', 'M', 32, 'Garcia', 'David', TRUE, TRUE,  '2024-03-05', '123 Birch St', 'OH', '44101', 'USA'),
-- (89012345, 'user8@outlook.com', '890-123-4567', 'F', 29, 'Miller', 'Sarah', FALSE, FALSE, '2024-03-04', '456 Redwood St', 'GA', '30301', 'USA'),
-- (90123456, 'user9@gmail.com', '901-234-5678', 'M', 26, 'Davis', 'Robert', TRUE, FALSE,  '2024-03-03', '789 Willow St', 'NC', '28201', 'USA'),
-- (01234567, 'user10@outlook.com', '012-345-6789', 'F', 31, 'Martinez', 'Linda', FALSE, TRUE,'2024-03-02', '321 Palm St', 'AZ', '85001', 'USA');

INSERT INTO UserPreference (PreferenceID, User_ID, Allowed_Sharing_Info, Allowed_Reciving_ADV, Allowed_Sending_Email, Allowed_Sending_text)
VALUES
(87654321, 6, TRUE, FALSE, TRUE, TRUE),
(98765432, 7, FALSE, TRUE, FALSE, TRUE),
(19876543, 8, TRUE, TRUE, TRUE, FALSE),
(21987654, 9, FALSE, FALSE, FALSE, TRUE);


INSERT INTO Auction (Auction_ID, Auction_Status, Start_Time, End_Time, Auction_Period, Attend_User_ID)
VALUES
(12345, 'open', '2024-03-11 10:00:00', NULL, NULL, 6),
(12346, 'open', '2024-03-11 10:00:00', NULL, NULL, 6),
(12347, 'open', '2024-03-11 10:00:00', NULL, NULL, 6),
(12348, 'open', '2024-03-11 10:00:00', NULL, NULL, 6),
(12349, 'open', '2024-03-11 10:00:00', NULL, NULL, 6),
(12350, 'open', '2024-03-11 10:00:00', NULL, NULL, 6);

INSERT INTO Car (VIN, Exterior_Color, Interior_Color, Make, Model, Fuel, Year, List_Time, List_Price, Current_Mileage)
VALUES
('1HGCM82633A004352', 'Black', 'Gray', 'Honda', 'Accord', 'Gasoline', 2018, '2024-03-11 10:00:00', 15000.00, 30000),
('1HGCM82633A004353', 'White', 'Black', 'Toyota', 'Camry', 'Hybrid', 2019, '2024-03-10 09:00:00', 18000.00, 25000),
('1HGCM82633A004354', 'Silver', 'Gray', 'Ford', 'Fusion', 'Electric', 2020, '2024-03-09 08:00:00', 22000.00, 20000),
('1HGCM82633A004355', 'Red', 'Black', 'Chevrolet', 'Impala', 'Gasoline', 2017, '2024-03-08 11:00:00', 14000.00, 35000),
('1HGCM82633A004356', 'Blue', 'Gray', 'Nissan', 'Altima', 'Hybrid', 2018, '2024-03-07 12:00:00', 16000.00, 28000),
('1HGCM82633A004357', 'Gray', 'Black', 'Hyundai', 'Sonata', 'Electric', 2019, '2024-03-06 13:00:00', 19000.00, 22000),
('1HGCM82633A004358', 'Black', 'Gray', 'Kia', 'Optima', 'Gasoline', 2020, '2024-03-05 14:00:00', 20000.00, 18000),
('1HGCM82633A004359', 'White', 'Black', 'Volkswagen', 'Passat', 'Hybrid', 2017, '2024-03-04 15:00:00', 13000.00, 40000),
('1HGCM82633A004360', 'Silver', 'Gray', 'BMW', '3 Series', 'Electric', 2018, '2024-03-03 16:00:00', 25000.00, 15000),
('1HGCM82633A004361', 'Red', 'Black', 'Audi', 'A4', 'Gasoline', 2019, '2024-03-02 17:00:00', 27000.00, 12000),
('1HGCM82633A004362', 'Blue', 'Black', 'Mazda', '6', 'Gasoline', 2018, '2024-03-01 10:00:00', 16000.00, 24000),
('1HGCM82633A004363', 'Green', 'Gray', 'Toyota', 'Prius', 'Hybrid', 2020, '2024-02-28 09:00:00', 19000.00, 21000),
('1HGCM82633A004364', 'Black', 'Black', 'Tesla', 'Model 3', 'Electric', 2021, '2024-02-27 08:00:00', 30000.00, 10000),
('1HGCM82633A004365', 'White', 'Gray', 'Honda', 'Civic', 'Gasoline', 2019, '2024-02-26 11:00:00', 17000.00, 27000),
('1HGCM82633A004366', 'Red', 'Black', 'Ford', 'Mustang', 'Gasoline', 2020, '2024-02-25 12:00:00', 25000.00, 15000),
('1HGCM82633A004367', 'Blue', 'Gray', 'Chevrolet', 'Volt', 'Electric', 2018, '2024-02-24 13:00:00', 18000.00, 22000),
('1HGCM82633A004368', 'Silver', 'Black', 'Nissan', 'Leaf', 'Electric', 2019, '2024-02-23 14:00:00', 20000.00, 18000),
('1HGCM82633A004369', 'Gray', 'Gray', 'Hyundai', 'Elantra', 'Gasoline', 2017, '2024-02-22 15:00:00', 14000.00, 30000),
('1HGCM82633A004370', 'Black', 'Black', 'Kia', 'Soul', 'Electric', 2021, '2024-02-21 16:00:00', 21000.00, 12000),
('1HGCM82633A004371', 'White', 'Gray', 'Volkswagen', 'Golf', 'Hybrid', 2020, '2024-02-20 17:00:00', 22000.00, 16000),
('1N4AL11D42C121723', 'Black', 'Black', 'Bugatti', 'Chiron', 'Gasoline', 2023, '2024-03-25 20:00:00', 4300000.00, 109),
('1TAN0000000000000', 'Yellow', 'Black', ' Chevrolet', 'Corvette', 'Gasoline', 2023, '2024-04-14 17:00:00', 180000.00, 715),
('1XPY1111111111111', 'Red', 'Black', 'Ferrari', '', 'LaFerrari', 'Gasoline', 2020, '2024-02-20 17:00:00', 2000000.00, 111);

-- INSERT INTO Sedan (VIN, SeatNumber)
-- VALUES
-- ('1HGCM82633A004352', 5),
-- ('1HGCM82633A004353', 5),
-- ('1HGCM82633A004355', 5),
-- ('1HGCM82633A004358', 5),
-- ('1HGCM82633A004359', 5);

-- INSERT INTO SUV (VIN, SeatNumber)
-- VALUES
-- ('1HGCM82633A004354', 7),
-- ('1HGCM82633A004356', 7),
-- ('1HGCM82633A004357', 7),
-- ('1HGCM82633A004360', 7),
-- ('1HGCM82633A004361', 7);

-- INSERT INTO Convertible (VIN, CanopyMaterial)
-- VALUES
-- ('1HGCM82633A004352', 'Fabric'),
-- ('1HGCM82633A004353', 'Hardtop'),
-- ('1HGCM82633A004355', 'Fabric'),
-- ('1HGCM82633A004358', 'Hardtop'),
-- ('1HGCM82633A004359', 'Fabric');


-- INSERT INTO Electric (VIN, Electric_Range)
-- VALUES
-- ('1HGCM82633A004354', 300),
-- ('1HGCM82633A004357', 350),
-- ('1HGCM82633A004360', 400);

-- INSERT INTO Hybrid (VIN, Fuel_Range, Electric_Range)
-- VALUES
-- ('1HGCM82633A004353', 500, 50),
-- ('1HGCM82633A004356', 550, 60),
-- ('1HGCM82633A004359', 600, 70);

-- INSERT INTO Truck (VIN, BoatLoad)
-- VALUES
-- ('1HGCM82633A004352', 2000),
-- ('1HGCM82633A004355', 2500),
-- ('1HGCM82633A004358', 3000),
-- ('1HGCM82633A004361', 3500);

INSERT INTO AuctionCar (Auction_id, VIN, Unsold, Reserve_Price, Start_Bid, SoldPrice)
VALUES
(12345, '1HGCM82633A004352', FALSE, 10500.00, 5200.00, NULL),
(12345, '1HGCM82633A004353', FALSE, 15500.00, 7700.00, NULL),
(12345, '1HGCM82633A004354', FALSE, 20500.00, 10500.00, NULL),
(12345, '1HGCM82633A004355', FALSE, 25500.00, 12500.00, NULL),
(12346, '1HGCM82633A004356', FALSE, 30500.00, 15500.00, NULL),
(12346, '1HGCM82633A004357', FALSE, 35500.00, 17500.00, NULL),
(12346, '1HGCM82633A004358', FALSE, 40500.00, 20500.00, NULL),
(12346, '1HGCM82633A004359', FALSE, 45500.00, 22500.00, NULL),
(12347, '1HGCM82633A004360', FALSE, 50500.00, 25500.00, NULL),
(12347, '1HGCM82633A004361', FALSE, 55500.00, 27500.00, NULL),
(12347, '1HGCM82633A004362', FALSE, 50500.00, 25500.00, NULL),
(12347, '1HGCM82633A004363', FALSE, 55500.00, 27500.00, NULL),
(12348, '1HGCM82633A004364', FALSE, 50500.00, 25500.00, NULL),
(12348, '1HGCM82633A004365', FALSE, 55500.00, 27500.00, NULL),
(12348, '1HGCM82633A004366', FALSE, 50500.00, 25500.00, NULL),
(12348, '1HGCM82633A004367', FALSE, 55500.00, 27500.00, NULL),
(12349, '1HGCM82633A004368', FALSE, 50500.00, 25500.00, NULL),
(12349, '1HGCM82633A004369', FALSE, 55500.00, 27500.00, NULL),
(12349, '1HGCM82633A004370', FALSE, 50500.00, 25500.00, NULL),
(12349, '1HGCM82633A004371', FALSE, 55500.00, 27500.00, NULL),
(12350, '1N4AL11D42C121723', FALSE, 50500.00, 250000.00, NULL),
(12350, '1TAN0000000000000', FALSE, 55500.00, 270000.00, NULL),
(12350, '1XPY1111111111111', FALSE, 50500.00, 290000.00, NULL);


INSERT INTO Bid (Bid_ID, User_ID, Auction_ID, Bid_Amount, Bid_Time, VIN, BIDWIN)
VALUES
(123456, 12345678, 12345, 12000.00, '2024-03-11 10:30:00', '1HGCM82633A004352', TRUE),
(234567, 23456789, 23456, 8000.00, '2024-03-10 09:30:00', '1HGCM82633A004353', FALSE),
(345678, 34567890, 34567, 22000.00, '2024-03-09 08:30:00', '1HGCM82633A004354', TRUE),
(456789, 45678901, 45678, 13000.00, '2024-03-08 11:30:00', '1HGCM82633A004355', FALSE),
(567890, 56789012, 56789, 32000.00, '2024-03-07 12:30:00', '1HGCM82633A004356', TRUE),
(678901, 67890123, 67890, 18000.00, '2024-03-06 13:30:00', '1HGCM82633A004357', FALSE),
(789012, 78901234, 78901, 42000.00, '2024-03-05 14:30:00', '1HGCM82633A004358', TRUE),
(890123, 89012345, 89012, 24000.00, '2024-03-04 15:30:00', '1HGCM82633A004359', FALSE),
(901234, 90123456, 90123, 52000.00, '2024-03-03 16:30:00', '1HGCM82633A004360', TRUE),
(012345, 01234567, 01234, 29000.00, '2024-03-02 17:30:00', '1HGCM82633A004361', FALSE);

INSERT INTO Orders (Order_ID, Time, Bidder, Seller, O_Price, Payment_Method, VIN, Auction_ID)
VALUES
(1234567, '2024-03-11 11:00:00', 12345678, 23456789, 12000.00, 'Credit Card', '1HGCM82633A004352', 12345),
(2345678, '2024-03-10 17:30:00', 34567890, 45678901, 22000.00, 'Debit Card', '1HGCM82633A004354', 34567),
(3456789, '2024-03-09 18:00:00', 56789012, 67890123, 32000.00, 'Cash', '1HGCM82633A004356', 56789),
(4567890, '2024-03-08 19:30:00', 78901234, 89012345, 42000.00, 'Bank Transfer', '1HGCM82633A004358', 78901),
(5678901, '2024-03-07 20:00:00', 90123456, 01234567, 52000.00, 'Credit Card', '1HGCM82633A004360', 90123),
(6789012, '2024-03-06 21:30:00', 12345678, 23456789, 8000.00, 'Debit Card', '1HGCM82633A004353', 23456),
(7890123, '2024-03-05 22:00:00', 34567890, 45678901, 13000.00, 'Cash', '1HGCM82633A004355', 45678),
(8901234, '2024-03-04 23:30:00', 56789012, 67890123, 18000.00, 'Bank Transfer', '1HGCM82633A004357', 67890),
(9012345, '2024-03-03 00:00:00', 78901234, 89012345, 24000.00, 'Credit Card', '1HGCM82633A004359', 89012),
(0123456, '2024-03-02 01:30:00', 90123456, 01234567, 29000.00, 'Debit Card', '1HGCM82633A004361', 01234);



INSERT INTO UserFeedback (Case_ID, Feedback, Category, ProvideFB_User_ID)
VALUES
(123456,  'Great experience', 'Positive', 12345678),
(234567,  'Could be better', 'Neutral', 23456789),
(345678,  'Excellent service', 'Positive', 34567890),
(456789, 'Not satisfied', 'Negative', 45678901),
(567890,  'Very helpful', 'Positive', 56789012),
(678901,  'Average experience', 'Neutral', 67890123),
(789012, 'Highly recommend', 'Positive', 78901234),
(890123,  'Disappointed', 'Negative', 89012345),
(901234,  'Good communication', 'Positive', 90123456),
(012345,  'Fair service', 'Neutral', 01234567);



INSERT INTO Payment (Payment_ID, User_ID, Payment_Method, Payment_Status)
VALUES
(12345678, 12345678, 'Credit Card', 'Completed'),
(23456789, 23456789, 'Debit Card', 'Pending'),
(34567890, 34567890, 'Bank Transfer', 'Completed'),
(45678901, 45678901, 'Cash', 'Failed'),
(56789012, 56789012, 'Credit Card', 'Completed'),
(67890123, 67890123, 'Debit Card', 'Pending'),
(78901234, 78901234, 'Bank Transfer', 'Completed'),
(89012345, 89012345, 'Cash', 'Failed'),
(90123456, 90123456, 'Credit Card', 'Completed'),
(01234567, 01234567, 'Debit Card', 'Pending');





INSERT INTO Report (Report_ID, VIN, Detail_History, Owner_History, Title_History, Additional_History, History_Mileage, Owner_Count)
VALUES
(12345, '1HGCM82633A004352', 'No accidents reported', '2 owners', 'Clean title', 'Regular maintenance', 30000, 2),
(23456, '1HGCM82633A004353', 'Minor fender bender', '1 owner', 'Clean title', 'New tires', 25000, 1),
(34567, '1HGCM82633A004354', 'No accidents reported', '3 owners', 'Clean title', 'Battery replaced', 20000, 3),
(45678, '1HGCM82633A004355', 'Rear-end collision', '2 owners', 'Salvage title', 'Engine rebuilt', 35000, 2),
(56789, '1HGCM82633A004356', 'No accidents reported', '1 owner', 'Clean title', 'Brakes replaced', 28000, 1),
(67890, '1HGCM82633A004357', 'Side-impact collision', '4 owners', 'Rebuilt title', 'Transmission replaced', 22000, 4),
(78901, '1HGCM82633A004358', 'No accidents reported', '2 owners', 'Clean title', 'Oil changes', 18000, 2),
(89012, '1HGCM82633A004359', 'Front-end collision', '3 owners', 'Salvage title', 'Suspension repaired', 40000, 3),
(90123, '1HGCM82633A004360', 'No accidents reported', '1 owner', 'Clean title', 'New battery', 15000, 1),
(01234, '1HGCM82633A004361', 'Minor scratches', '2 owners', 'Clean title', 'Tire rotation', 12000, 2);


INSERT INTO Shipping (Tracking_Number, Shipping_Method, Shipping_Status, Car_VIN, User_ID_Track, Approved_Payment_ID)
VALUES
('TRACK12345', 'Standard', 'Delivered', '1HGCM82633A004352', 12345678, 12345678),
('TRACK23456', 'Expedited', 'In Transit', '1HGCM82633A004353', 34567890, 34567890),
('TRACK34567', 'Standard', 'Delivered', '1HGCM82633A004354', 56789012, 56789012),
('TRACK45678', 'Express', 'In Transit', '1HGCM82633A004355', 78901234, 78901234),
('TRACK56789', 'Standard', 'Delivered', '1HGCM82633A004356', 90123456, 90123456);



INSERT INTO Admin (Admin_ID, SSN, Name, Birthdate)
VALUES
(1, '123-45-6789', 'Alice Johnson', '1975-04-12'),
(2, '234-56-7890', 'Bob Smith', '1980-05-23'),
(3, '345-67-8901', 'Charlie Brown', '1972-06-30'),
(4, '456-78-9012', 'Diana Ross', '1968-07-15'),
(5, '567-89-0123', 'Ethan Hunt', '1985-08-28'),
(6, '678-90-1234', 'Fiona Gallagher', '1990-09-10'),
(7, '789-01-2345', 'George Lucas', '1973-10-14'),
(8, '890-12-3456', 'Hannah Montana', '1982-11-20'),
(9, '901-23-4567', 'Ian Somerhalder', '1978-12-08'),
(10, '012-34-5678', 'Julia Roberts', '1967-01-29');

INSERT INTO Manage (Admin_ID, Password)
VALUES
(1, 'password1' ),
(2, 'password2'),
(3, 'password3'),
(4, 'password4'),
(5, 'password5'),
(6, 'password6'),
(7, 'password7'),
(8, 'password8'),
(9, 'password9'),
(10, 'password10');


INSERT INTO Transaction (Payment_ID, Order_ID, Transaction_ID, Payment_Method, Time, Transaction_Amount)
VALUES
(12345678, 1234567, 1, 'Credit Card', '2024-03-11 11:30:00', 12000.00),
(23456789, 2345678, 2, 'Debit Card', '2024-03-10 18:00:00', 22000.00),
(34567890, 3456789, 3, 'Bank Transfer', '2024-03-09 18:30:00', 32000.00),
(45678901, 4567890, 4, 'PayPal', '2024-03-08 20:00:00', 42000.00),
(56789012, 5678901, 5, 'Cash', '2024-03-07 20:30:00', 52000.00),
(67890123, 6789012, 6, 'Credit Card', '2024-03-06 22:00:00', 8000.00),
(78901234, 7890123, 7, 'Debit Card', '2024-03-05 22:30:00', 13000.00),
(89012345, 8901234, 8, 'Bank Transfer', '2024-03-04 00:00:00', 18000.00),
(90123456, 9012345, 9, 'PayPal', '2024-03-03 00:30:00', 24000.00),
(01234567, 0123456, 10, 'Cash', '2024-03-02 02:00:00', 29000.00);


