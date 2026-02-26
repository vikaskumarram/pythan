
## Review 1 — Tasks
- List all the Canadian      
  cities and their populations
  Order all the cities in the United States by their latitude from north to south

  ```sql
  SELECT  city, country, population
  FROM north_american_cities
  WHERE country = "Canada";
 ```
- List all the cities west of Chicago, ordered from west to east

 '''sql
 SELECT city,latitude
 FROM north_american_cities
 WHERE country = "United States"
 ORDER BY latitude desc;
 '''


- List the two largest cities in Mexico (by population)
'''sql

'''
- List the third and fourth largest cities (by population) in the   United States and their population

- every table start with denormalization then becaome normalization
