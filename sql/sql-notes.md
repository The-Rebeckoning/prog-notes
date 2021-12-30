# CASE functions

Function returns a value that’s determined by the conditions you specify 

*syntax*

	
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


# The SQL LIKE Operator
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:

 The percent sign (%) represents zero, one, or multiple characters
 The underscore sign (_) represents one, single character


	SELECT column1, column2, ...
	FROM table_name
	WHERE columnN LIKE pattern;

# LIKE Operator			Description
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

	SELECT select_list
	FROM table_source
	WHERE search_condition
	[GROUP BY group_by_list]
	[HAVING search_condition]
	[ORDER BY order_by_list]



# How to use the WITH ROLLUP operator 

WITH ROLLUP operator in the GROUP BY clause to add summary rows to the final result set. The row summarizes the aggregate columns in the result set 


SQL ROLLUP with partial rollup example
You can use ROLLUP to perform a partial roll-up that reduces the number of subtotals calculated as shown in the following example:

	SELECT 
    		warehouse, product, SUM(quantity)
	FROM
    		inventory

	GROUP BY warehouse, ROLLUP (product);
##ROUND

Returns the number rounded to the precision specified by length. If length is 0 the decimal digits are omitted.

  ROUND (number[,length]

# Different types of Joins:
- (Inner) Join
- Left (Outer) Join
- Full (Outer) Join


