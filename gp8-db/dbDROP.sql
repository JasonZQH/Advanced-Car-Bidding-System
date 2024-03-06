-- Create a script that will drop all the objects you have created for your project including table, trigger, index, and etc..  
-- This will be used to start from a clean state after some inserts and deletes have been added to your application to check the correctness of your queries.  
-- You should be able to clean everything through this script and re-create the database instance.

-- Be sure to have a backup of your data before running this script

-- Drop the view
DROP VIEW IF EXISTS WinningBids;

-- Drop the function
DROP PROCEDURE IF EXISTS AddNewUser;

-- Drop the trigger
DROP TRIGGER IF EXISTS CloseAuction;

-- Drop the tables. The order is important due to foreign key constraints.
DROP TABLE IF EXISTS Report;
DROP TABLE IF EXISTS Shipping;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Manage;
DROP TABLE IF EXISTS Truck;
DROP TABLE IF EXISTS Hybrid;
DROP TABLE IF EXISTS Electric;
DROP TABLE IF EXISTS Convertible;
DROP TABLE IF EXISTS SUV;
DROP TABLE IF EXISTS Sedan;
DROP TABLE IF EXISTS Car;
DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS UserFeedback;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Bid;
DROP TABLE IF EXISTS Auction;
DROP TABLE IF EXISTS Payment;
DROP TABLE IF EXISTS Users;

