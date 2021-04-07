SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.Temperature > w2.Temperature
    AND TO_DAYS(w1.recordDate) - TO_DAYS(w2.recordDate) = 1;