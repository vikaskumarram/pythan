'''
 ## Exercise 1 — Tasks
- Find the title of each film ✓
 '''
 title
Toy Story
A Bug's Life
Toy Story 2
Monsters, Inc.
Finding Nemo
The Incredibles
Cars
Ratatouille
WALL-E
Up
Toy Story 3
Cars 2
Brave
Monsters University
 '''


- Find the director of each film
  '''
  director
John Lasseter
John Lasseter
John Lasseter
Pete Docter
Andrew Stanton
Brad Bird
John Lasseter
Brad Bird
Andrew Stanton
Pete Docter
Lee Unkrich
John Lasseter
Brenda Chapman
Dan Scanlon
  '''
- Find the title and director of each film
  '''
title	director
Toy Story	John Lasseter
A Bug's Life	John Lasseter
Toy Story 2	John Lasseter
Monsters, Inc.	Pete Docter
Finding Nemo	Andrew Stanton
The Incredibles	Brad Bird
Cars	John Lasseter
Ratatouille	Brad Bird
WALL-E	Andrew Stanton
Up	Pete Docter
Toy Story 3	Lee Unkrich
Cars 2	John Lasseter
Brave	Brenda Chapman
Monsters University	Dan Scanlon

  '''
- Find the title and year of each film
'''
title	year
Toy Story	1995
A Bug's Life	1998
Toy Story 2	1999
Monsters, Inc.	2001
Finding Nemo	2003
The Incredibles	2004
Cars	2006
Ratatouille	2007
WALL-E	2008
Up	2009
Toy Story 3	2010
Cars 2	2011
Brave	2012
Monsters University	2013
'''
Find all the information about each film ✓
'''
Find all the information about each film ✓
'''
![alt text](<Screenshot 2026-02-25 161421.png>)



## Exercise 2 — Tasks
- Find the movie with a row id of 6 ✓
SELECT * 
FROM movies 
WHERE id = 6;

- Find the movies released in the years between 2000 and 2010
  SELECT *
FROM movies
WHERE YEAR BETWEEN 2000 AND 2010;

- Find the movies not released in the years between 2000 and 2010
  SELECT *
FROM movies
WHERE YEAR NOT BETWEEN 2000 AND 2010;
- Find the first 5 Pixar movies and their release year
  SELECT *
FROM movies
WHERE ID <6;
'''
Exercise 2 — Tasks
Find the movie with a row id of 6 ✓
Find the movies released in the years between 2000 and 2010 ✓
Find the movies not released in the years between 2000 and 2010 ✓
Find the first 5 Pixar movies and their release year ✓
'''



## Exercise 3 — Tasks
- Find all the Toy Story movies
  SELECT * 
FROM movies
WHERE TITLE LIKE "Toy Story%";


- Find all the movies directed by John Lasseter
 SELECT * 
FROM movies
WHERE director LIKE "John Lasseter%";


- Find all the movies (and director) not directed by John Lasseter
  SELECT * 
FROM movies
WHERE director not like "john Lasseter%";


- Find all the WALL-* movies
  SELECT * 
FROM movies
WHERE title like "WALL%";

![alt text](<Screenshot 2026-02-25 172209.png>)

Exercise 3 — Tasks
Find all the Toy Story movies ✓
Find all the movies directed by John Lasseter ✓
Find all the movies (and director) not directed by John Lasseter ✓
Find all the WALL-* movies ✓



## Exercise 4 — Tasks

- List all directors of Pixar movies (alphabetically), without duplicates
  SELECT DISTINCT DIRECTOR
 FROM movies
 ORDER BY DIRECTOR ASC;


- List the last four Pixar movies released (ordered from most - recent to least)
 SELECT TITLE,YEAR
FROM movies
ORDER BY  YEAR DESC
LIMIT 4;


- List the first five Pixar movies sorted alphabetically
  SELECT TITLE 
FROM movies
ORDER BY TITLE ASC
LIMIT 5
;


- List the next five Pixar movies sorted alphabetically
  SELECT TITLE 
FROM movies
ORDER BY TITLE ASC
LIMIT 5 OFFSET 5
;

(<Screenshot 2026-02-25 181932.png>)

## Exercise 4 — Tasks
List all directors of Pixar movies (alphabetically), without duplicates ✓

List the last four Pixar movies released (ordered from most recent to least) ✓

List the first five Pixar movies sorted alphabetically ✓

List the next five Pixar movies sorted alphabetically ✓