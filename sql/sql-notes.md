# CASE functions

Function returns a value that’s determined by the conditions you specify 

*syntax*

	
	CASE input_expression
		WHEN when_expression_1 THEN result_expression_1
		WHEN when_expression_1 THEN result_expression_2
		ELSE else_result_expression


## Example

	SELECT player_name, weight,
       		CASE WHEN weight > 250 THEN 'over 250'
            	WHEN weight > 200 THEN '201-250'
            	WHEN weight > 175 THEN '176-200'
            	ELSE '175 or under' END AS weight_group
  	FROM benn.college_football_players

