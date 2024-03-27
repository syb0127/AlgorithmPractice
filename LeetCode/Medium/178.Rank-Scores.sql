SELECT score, dense_rank() over (ORDER BY score DESC) 'rank'
FROM Scores