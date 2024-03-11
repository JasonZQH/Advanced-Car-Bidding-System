-- Create a script with queries from the relation algebra in Step 7, named dbSQL.sql. 
-- This script should contain at least 5 queries on your database. 
-- Use the comment facility in mysql script to write the English version of your query, followed by the SQL version of the query. 
-- Also show the expected output in the file. 

-- These queries need to satisfy the following:
-- Should be at least join queries (some involving more than 2 relations)
-- At least two of them should be aggregate queries including GROUP BY and HAVING clauses with ORDER BY clause as well
-- At least one of them should have subquery (either inline view, nested or with)

-- English: Get users who won a bid in auctions with auction and bid details
SELECT u.User_ID, u.FirstN, u.LastN, a.Auction_ID, a.Auction_Status, b.Bid_Amount, b.BIDWIN
FROM Users u
JOIN Bid b ON u.User_ID = b.User_ID
JOIN Auction a ON b.Auction_ID = a.Auction_ID
WHERE b.BIDWIN = TRUE;

-- English: Get total bids and average bid amount for each closed auction
SELECT a.Auction_ID, COUNT(b.Bid_ID) AS Total_Bids, AVG(b.Bid_Amount) AS Average_Bid
FROM Auction a
JOIN Bid b ON a.Auction_ID = b.Auction_ID
WHERE a.Auction_Status = 'closed'
GROUP BY a.Auction_ID;

-- English: Get auctions with an average bid amount higher than the overall average
SELECT a.Auction_ID, AVG(b.Bid_Amount) AS Average_Bid
FROM Auction a
JOIN Bid b ON a.Auction_ID = b.Auction_ID
GROUP BY a.Auction_ID
HAVING AVG(b.Bid_Amount) > (SELECT AVG(Bid_Amount) FROM Bid);

-- English: Get users bid in open auctions
SELECT u.User_ID, u.FirstN, u.LastN, COUNT(b.Bid_ID) AS Bid_Count
FROM Users u
JOIN Bid b ON u.User_ID = b.User_ID
JOIN Auction a ON b.Auction_ID = a.Auction_ID
WHERE a.Auction_Status = 'open'
GROUP BY u.User_ID
HAVING COUNT(b.Bid_ID) > 0;

-- English: Get top 3 highest list price cars that are unsold in auctions
SELECT c.VIN, c.Make, c.Model, c.List_Price
FROM Car c
JOIN AuctionCar ac ON c.VIN = ac.VIN
WHERE ac.Unsold = TRUE
ORDER BY c.List_Price DESC
LIMIT 3;

-- English: Get users who have bid on a specific make and won at least one auction
SELECT DISTINCT u.User_ID, u.FirstN, u.LastN
FROM Users u
WHERE EXISTS (
    SELECT 1
    FROM Bid b
    JOIN AuctionCar ac ON b.VIN = ac.VIN
    JOIN Car c ON ac.VIN = c.VIN
    WHERE b.User_ID = u.User_ID AND c.Make = 'Honda' AND b.BIDWIN = TRUE
);

