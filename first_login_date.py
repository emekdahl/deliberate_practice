SELECT player_id, min(event_date) AS first_login
FROM Activity
GROUP BY player_id

# using min was a better choice here than trying to order by