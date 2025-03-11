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
