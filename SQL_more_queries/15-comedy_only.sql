-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql) Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title
  FROM tv_shows AS t
       INNER JOIN tv_show_genres AS s
       ON t.id = s.show_id

       INNER JOIN tv_genres AS g
       ON g.id = s.genre_id
       WHERE g.name = "Comedy"
 ORDER BY t.title;
