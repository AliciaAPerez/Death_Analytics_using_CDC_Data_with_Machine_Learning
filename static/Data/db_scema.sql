-- DROP TABLE IF EXISTS cdc_death_table;
-- Create Death Data Table
CREATE TABLE cdc_death_table (
	icd_death_code VARCHAR,
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
	entity_condition_1 VARCHAR,
	entity_condition_2 VARCHAR,
	entity_condition_3 VARCHAR,
	race INT,
	hispanic INT,
	id BIGSERIAL PRIMARY KEY NOT NULL 
);

-- DROP TABLE IF EXISTS life_expectancy;
-- Create life_expectancy Table
CREATE TABLE life_expectancy (
	year VARCHAR,
	race VARCHAR,
	sex VARCHAR,
	average_life_expectancy VARCHAR,
	age_adjusted_rate VARCHAR,
	id BIGSERIAL PRIMARY KEY NOT NULL 
);

-- DROP TABLE IF EXISTS leading_causes_death;
-- Create leading_causes_death Table
CREATE TABLE leading_causes_death (
	year VARCHAR,
	cause VARCHAR,
	cause_name VARCHAR,
	state VARCHAR,
	deaths VARCHAR,
	age_adjusted_death_rate VARCHAR,
	id BIGSERIAL PRIMARY KEY NOT NULL 
);

-- DROP TABLE IF EXISTS UN_Data;
-- Create UN_Data Table
CREATE TABLE UN_Data (
	Country VARCHAR,
	Year VARCHAR,
	Area VARCHAR,
	Sex VARCHAR,
	Age VARCHAR,
	Cause_of_Death_WHO VARCHAR,
	Value VARCHAR,
	id BIGSERIAL PRIMARY KEY NOT NULL 
);