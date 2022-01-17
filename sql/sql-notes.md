

# UPDATE

Modify data in one or more rows of a table. Can modify a specific row or multiple rows

	UPDATE table_name
	SET column_name1=expression_1
	WHERE search_condition
	UPDATE inhabitan
	t SET name = 'Reb' WHERE personid = 20


# Aggregate functions

An aggregate function performs a calculation on a set of values, and returns a single value. Except for COUNT(*), aggregate functions ignore null values. Aggregate functions are often used with the GROUP BY clause of the SELECT statement.

## AVG

The AVG() function returns the average value of a numeric column. 

The following SQL statement finds the average price of all products:

	SELECT AVG(Price)
	FROM Products;

### How to Filter Records with Aggregate Function AVG

You want to find groups of rows in which the average of values in a column is higher or lower than a given value.

	SELECT name, AVG(price)
	FROM product
	GROUP BY name
	HAVING AVG(price)>3.00;

## MAX

Our database has a table named student with data in the following columns: id, first_name, last_name, and grade.

	id	first_name	last_name	grade
	1	Lisa		Jackson		3
	2	Gary		Larry		5
	3	Tom			Michelin	2
	4	Martin		Barker		2
	5	Ellie		Black		5
	6	Mary		Simpson		4

Let’s find the students who have the highest grades.


	SELECT  id, first_name, last_name, grade
	FROM student
	WHERE grade = (SELECT MAX(grade) FROM student);


## MIN

You want to find rows that store the smallest numeric value in a column.

Our database has a table named weather with data in the following columns: id, city, and temperature.

	id	city		temperature
	1	Houston		23
	2	Atlanta		20
	3	Boston		15
	4	Cleveland	15
	5	Dallas		34
	6	Austin		28

Here’s how to find cities with the lowest temperature.


	SELECT  id, city, temperature
	FROM weather
	WHERE temperature = (SELECT MIN(temperature) FROM weather);

## SUM

The SUM() function returns the total sum of a numeric column. 

The following SQL statement finds the sum of the "Quantity" fields in the "OrderDetails" table:

	SELECT SUM(Quantity)
	FROM OrderDetails;

### How to Filter Records with Aggregate Function SUM

You need to find rows in which groups have a sum of values in one column less than a given value.

Let’s find the names of departments that have sums of salaries of its employees less than 7000.

Our database has a table named company with data in the following columns: id, department, first_name, last_name, and salary.

	id	department	first_name	last_name	salary
	1	marketing	Lora		Brown		2300
	2	finance		John		Jackson		3200
	3	marketing	Michael		Thomson		1270
	4	production	Tony		Miller		6500
	5	production	Sally		Green		2500
	6	finance		Olivier		Black		3450
	7	production	Jeniffer	Michelin	2800
	8	marketing	Jeremy		Lorson		3600
	9	marketing	Louis		Smith		4200

Let’s find the names of departments that have sums of salaries of its employees less than 7000.


	SELECT department, SUM(salary)
	FROM company
	GROUP BY department
	HAVING SUM(salary)<7000;


## COUNT

The COUNT() function returns the number of rows that matches a specified criterion.

The following SQL statement finds the number of products:

	SELECT COUNT(ProductID)
	FROM Products;

### How to Filter Records with Aggregate Function COUNT

You want to find groups of rows with a specific number of entries in a group.

Our database has a table named product with data in the following columns: id, name and category.

	id	name		category
	1	sofa		furniture
	2	gloves		clothing
	3	T-Shirt		clothing
	4	chair		furniture
	5	desk		furniture
	6	watch		electronics
	7	armchair	furniture
	8	skirt		clothing
	9	radio 		electronics

Let’s find the category of products with more than two entries.

	SELECT category, COUNT(id)
	FROM product
	GROUP BY category
	HAVING COUNT(id)>2;

# The SQL SELECT DISTINCT Statement

The SELECT DISTINCT statement is used to return only distinct (different) values.

Inside a table, a column often contains many duplicate values; and sometimes you only want to list the different (distinct) values.

The following SQL statement selects all (including the duplicates) values from the "Country" column in the "Customers" table:

	SELECT Country FROM Customers;

The following SQL statement lists the number of different (distinct) customer countries:

	SELECT COUNT(DISTINCT Country) FROM Customers;





# CASE functions

Function returns a value that’s determined by the conditions you specify 

## Syntax
	
	CASE input_expression
		WHEN when_expression_1 THEN result_expression_1
		WHEN when_expression_1 THEN result_expression_2
		ELSE else_result_expression


## Examples

	SELECT player_name, weight,
       		CASE WHEN weight > 250 THEN 'over 250'
            	WHEN weight > 200 THEN '201-250'
            	WHEN weight > 175 THEN '176-200'
            	ELSE '175 or under' END AS weight_group
  	FROM benn.college_football_players



	SELECT Name,
	CASE WHEN Occupation LIKE 'P%' THEN"(P)"
    		WHEN Occupation LIKE 'D%' THEN "(D)"
    		WHEN Occupation LIKE 'S%' THEN "(S)"
    	ELSE "(A)" END AS occupation_search
	FROM Occupations;


# concat ()

The CONCAT() function adds two or more strings together.

	SELECT CONCAT('SQL', ' is', ' fun!');
	
	SQL is fun!

# The SQL LIKE Operator
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

 The percent sign (%) represents zero, one, or multiple characters
 The underscore sign (_) represents one, single character


	SELECT column1, column2, ...
	FROM table_name
	WHERE columnN LIKE pattern;

# LIKE Operator						Description
	WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
	WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
	WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
	WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
	WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
	WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
	WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"


# How to code the GROUP BY and HAVING clauses

GROUP BY groups the rows of a result set based on one or more columns or expressions

HAVING lets you specify a search condition for a group or an aggregate 

## syntax

	SELECT select_list
	FROM table_source
	WHERE search_condition
	[GROUP BY group_by_list]
	[HAVING search_condition]
	[ORDER BY order_by_list]

## example

Let’s find the number of classes with more than five students.

	SELECT class
	FROM Courses
	GROUP BY class
	HAVING COUNT(student) >4

# How to use the WITH ROLLUP operator 

WITH ROLLUP operator in the GROUP BY clause to add summary rows to the final result set. The row summarizes the aggregate columns in the result set 


SQL ROLLUP with partial rollup example
You can use ROLLUP to perform a partial roll-up that reduces the number of subtotals calculated as shown in the following example:

	SELECT 
    		warehouse, product, SUM(quantity)
	FROM
    		inventory

	GROUP BY warehouse, ROLLUP (product);

## ROUND

Returns the number rounded to the precision specified by length. If length is 0 the decimal digits are omitted.

  ROUND (number[,length]

# Different types of Joins:

A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

- (Inner) Join
- Left (Outer) Join
- Full (Outer) Join
- Self Join

![Different types of joins](https://cdn.educba.com/academy/wp-content/uploads/2019/10/Types-of-Joins-in-SQl.png)

## Inner Join

### Syntax

	SELECT column_name(s)
	FROM table1
	INNER JOIN table2
	ON table1.column_name = table2.column_name;	

### Example

The following SQL statement selects all orders with customer information:

	SELECT Orders.OrderID, Customers.CustomerName
	FROM Orders
	INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

Note: The INNER JOIN keyword selects all rows from both tables as long as there is a match between the columns. If there are records in the "Orders" table that do not have matches in "Customers", these orders will not be shown!

## Left Join

The LEFT JOIN keyword returns all records from the left table (table1), and the matching records from the right table (table2). The result is 0 records from the right side, if there is no match.

### Syntax

	SELECT column_name(s)
	FROM table1
	LEFT JOIN table2
	ON table1.column_name = table2.column_name;

### Example

	SELECT Customers.CustomerName, Orders.OrderID
	FROM Customers
	LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
	ORDER BY Customers.CustomerName;

The LEFT JOIN keyword returns all records from the left table (Customers), even if there are no matches in the right table (Orders).

## Right Join

The RIGHT JOIN keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match

### Syntax

	SELECT column_name(s)
	FROM table1
	RIGHT JOIN table2
	ON table1.column_name = table2.column_namel

### Example

The following SQL statement will return all employees, and any orders they might have placed:

	SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
	FROM Orders
	RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
	ORDER BY Orders.OrderID;

The RIGHT JOIN keyword returns all records from the right table (Employees), even if there are no matches in the left table (Orders).

## Self Join

A self join is a regular join, but the table is joined with itself.

### Syntax

	SELECT column_name(s)
	FROM table1 T1, table1 T2
	WHERE condition;

### Example

The following SQL statement matches customers that are from the same city:


	SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
	FROM Customers A, Customers B
	WHERE A.CustomerID <> B.CustomerID
	AND A.City = B.City
	ORDER BY A.City;

