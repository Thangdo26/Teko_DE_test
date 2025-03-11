SELECT
    CustomerID,
    TransactionID,
    TransactionAmount,
    TransactionDate
FROM
(
    SELECT
        t.*,
        ROW_NUMBER() OVER (
            PARTITION BY t.CustomerID
            ORDER BY t.TransactionDate ASC
        ) AS rn
    FROM Transactions t
) AS sub
WHERE rn = 1
ORDER BY CustomerID;

/* Cách 2: Dùng subquery kết hợp MIN(TransactionDate) nếu có bảng Customers
SELECT 
    t.CustomerID,
    t.TransactionID,
    t.TransactionAmount,
    t.TransactionDate
FROM Transactions t
INNER JOIN 
(
    SELECT 
        CustomerID, 
        MIN(TransactionDate) AS MinDate
    FROM Transactions
    GROUP BY CustomerID
) AS sub 
    ON t.CustomerID = sub.CustomerID
    AND t.TransactionDate = sub.MinDate
ORDER BY t.CustomerID;
*/
