-- Create Death Data Table
CREATE TABLE cdc_death_table (
	resident INT,
	education INT,
	month_of_death INT,
	sex VARCHAR,
	age INT,
	marital_status VARCHAR,
	day_of_week_of_death INT,
	current_data_year INT,
	injury_at_work VARCHAR,
	manner_of_death INT,
	icd_death_code VARCHAR,
	entity_condition_1 VARCHAR,
	entity_condition_2 VARCHAR,
	entity_condition_3 VARCHAR,
	race INT,
	hispanic INT,
	id INT PRIMARY KEY NOT NULL 
);