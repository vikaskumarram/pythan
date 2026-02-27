
## Exercise 9 — Tasks
- List all movies and their combined sales in millions of dollars ✓
```sql
SELECT  distinct title, (domestic_sales + international_sales)/1000000
FROM movies
join boxoffice 
on movies.id = boxoffice.movie_id;
```
- List all movies and their ratings in percent
```sql
SELECT  distinct title, rating * 10
FROM movies
join boxoffice 
on movies.id = boxoffice.movie_id;
```
- List all movies that were released on even number years
```sql
SELECT  distinct title, year  
FROM movies
join boxoffice 
on movies.id = boxoffice.movie_id
where year%2 = 0;
```