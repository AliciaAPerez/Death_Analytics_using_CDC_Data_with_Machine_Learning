# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the username and password parameters are "postgres"
# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/
import psycopg2
from dbconfig import ADDRESS, PORT, DATABASE, USER, PASSWORD
# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell
# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")
# Or:
cn = psycopg2.connect(host=ADDRESS, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
# Create a cursor object
cur = cn.cursor()
# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""SELECT * FROM cdc_death_table limit 1000;""")
query_results = cur.fetchall()
print(query_results)
# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
cn.close()

# mode = "append"
# jdbc_url="jdbc:postgresql://database-1.ck7rneirj52d.us-east-2.rds.amazonaws.com:5432/Death_Database"
# config = {"user":"root", 
#           "password": "postgres", 
#           "driver":"org.postgresql.Driver"}