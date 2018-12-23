create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select a.name, b.size 
  from dogs as a, sizes as b 
  where a.height > b.min and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
	select child from parents, dogs where name = parent order by - height;
--  select name 
--  from dogs, parents
--  where name = child
--  order by height desc;

-- Sentences about siblings that are the same size
create table sentences as
	with
	siblings(x, y) as (
	select a.child, b.child 
	from parents as a, parents as b
	where a.parent = b.parent and a.child < b.child 
	order by b.child -- or a.child desc
	)
	select x || " and " || y || " are " || a.size || " siblings" from size_of_dogs as a, size_of_dogs as b, siblings where a.size = b.size and x = a.name and y = b.name; --dealing with whats inside of a single row

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
	with
	add_stacks(last_dog, last_height, lst, sum_height, n) as (
	select name, height, name, height, 1 from dogs union
	select name, height, lst || ', ' || name, height + sum_height, n + 1 
	from dogs, add_stacks
	where height >= last_height and name != last_dog and n <= 4
	)
  select lst, sum_height from add_stacks
  where sum_height >= 170 and n = 4
  order by sum_height;

-- Heights and names of dogs that are above average in height among
-- dogs whose height has the same first digit.
create table above_average as
	with average(avg_height, first_digit) as (
	select avg(height), height / 10
	from dogs
	group by height / 10
	)
    select height, name from dogs, average where height > avg_height and height / 10 = first_digit;
	

-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

-- Question 1: Composites --
create table composites as
	--select a.n from ints as a where a.n > 1 and a.n <= 100, Q. 
--how is it a.n and b.n get different set of numbers respectively?, difference between distinct and n1 > n2? aside from the fact that group by is same the distinct to get rid of duplicates. > will filter out the duplicate pair, and distinct will get rid of duplicated numbers. count w/out groupby treats every row distinctively, and retruns the number of rows whereas with groupby you grab identical row as one and return number of the rows by groups.
-- whats the difference between with and a.obj
	select distinct a.n * b.n as c from ints as a, ints as b where a.n > 1 and b.n > 1 and a.n * b.n <= 100;

create table multiples as
   select c as m from composites union all select n from ints;

-- Question 2: Primes --
create table primes as
   select m as p from multiples where p > 1 group by p having count(*) = 1; --has only count of 1
   -- where, group by, having
