-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql) Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT t.title, g.name
  FROM tv_shows AS t
       LEFT JOIN tv_show_genres AS s
       ON t.id = s.show_id

       LEFT JOIN tv_genres AS g
       ON s.genre_id = g.id
 ORDER BY t.title, g.name;
