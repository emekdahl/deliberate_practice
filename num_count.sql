SELECT DISTINCT Num as ConsecutiveNums
FROM
    (
        SELECT Id
            , Num
            , Lead(Num, 1) OVER(ORDER BY Id) as NextNum
            , Lead(Num, 2) OVER(ORDER BY Id) as NextNum2
        FROM Logs
    ) A
WHERE Num = NextNum and Num = NextNum2

-- https://www.geeksforgeeks.org/sql-server-lead-function-overview/

-- lead allows me to select a specified number of rows beforehand