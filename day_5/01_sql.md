
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
![alt text](<Screenshot 2026-02-27 120903.png>)

## Exercise 10 — Tasks

- Find the longest time that an employee has been at the studio ✓
```sql
SELECT MAX(years_employed) as Max_years_employed
FROM employees;
```
- For each role, find the average number of years employed by employees in that role
```sql
SELECT role, AVG(years_employed) as Average_years_employed
FROM employees
GROUP BY role;
```

- Find the total number of employee years worked in each building
```sql
SELECT building, SUM(years_employed) as Total_years_employed
FROM employees
GROUP BY building;
```
![alt text](<Screenshot 2026-02-27 124812.png>)