CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents, dogs WHERE parent = name ORDER BY height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child as first, b.child as second, c.size as size
  FROM parents AS a, parents AS b, size_of_dogs AS c, size_of_dogs AS d 
  WHERE a.parent = b.parent AND c.size = d.size AND c.name = a.child AND d.name = b.child AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT first || " and " || second || " are " || size || " siblings" FROM siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height

CREATE TABLE stacks AS
  SELECT a.name || ", " || b.name || ", " || c.name || ", " || d.name,
  a.height + b.height + c.height + d.height as stack_height
  FROM dogs AS a, dogs AS b, dogs AS c, dogs AS d 
  WHERE a.height + b.height + c.height + d.height> 170 
    AND a.height < b.height AND b.height < c.height AND c.height < d.height
  ORDER BY stack_height
