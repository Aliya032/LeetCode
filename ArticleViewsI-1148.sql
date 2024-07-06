-- 06-07-2024 19:09
-- https://leetcode.com/problems/article-views-i
-- https://www.youtube.com/watch?v=KJ0kmu7NbBI
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
