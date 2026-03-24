
Customer Sales Analytics Project
Author: Piyush Ahirwar
Database: newschema | Table: custome


-- 1. REVENUE BY PRODUCT
SELECT Product,
    COUNT(*) AS TotalOrders,
    SUM(Quantity) AS UnitsSold,
    ROUND(SUM(Quantity * UnitPrice), 2) AS TotalRevenue
FROM customer
GROUP BY Product
ORDER BY TotalRevenue DESC;

-- 2. MONTHLY SALES TREND
SELECT 
    DATE_FORMAT(PurchaseDate, '%Y-%m') AS Month,
    ROUND(SUM(Quantity * UnitPrice), 2) AS MonthlySales
FROM customer
GROUP BY Month
ORDER BY Month;

-- 3. CUSTOMER SEGMENTATION
SELECT CustomerID,
    ROUND(SUM(Quantity * UnitPrice), 2) AS TotalSpend,
    CASE 
        WHEN SUM(Quantity * UnitPrice) > 8000 THEN 'Premium'
        WHEN SUM(Quantity * UnitPrice) > 5000 THEN 'Regular'
        ELSE 'Low Value'
    END AS Segment
FROM customer
GROUP BY CustomerID
ORDER BY TotalSpend DESC;

-- 4. SEGMENT COUNT
SELECT Segment, COUNT(*) AS CustomerCount
FROM (
    SELECT CustomerID,
        CASE 
            WHEN SUM(Quantity * UnitPrice) > 8000 THEN 'Premium'
            WHEN SUM(Quantity * UnitPrice) > 5000 THEN 'Regular'
            ELSE 'Low Value'
        END AS Segment
    FROM customer
    GROUP BY CustomerID
) AS seg
GROUP BY Segment;

-- 5. TOP 10 CUSTOMERS
SELECT CustomerID,
    COUNT(*) AS Orders,
    ROUND(SUM(Quantity * UnitPrice), 2) AS TotalSpend
FROM customer
GROUP BY CustomerID
ORDER BY TotalSpend DESC
LIMIT 10;

-- 6. RFM ANALYSIS
SELECT CustomerID,
    DATEDIFF(NOW(), MAX(PurchaseDate)) AS Recency,
    COUNT(*) AS Frequency,
    ROUND(SUM(Quantity * UnitPrice), 2) AS Monetary
FROM customer
GROUP BY CustomerID
ORDER BY Monetary DESC;
