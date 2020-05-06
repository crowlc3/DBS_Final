import psycopg2
import csv
import os

db_port = os.getenv('db_port') or '5432';
connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password' port=" + db_port;
conn = psycopg2.connect(connection_string)

# Build the schema based on the schema file
def buildSchema():
	with conn.cursor() as cursor:
		setup_queries = open('schema.sql', 'r').read()
		cursor.execute(setup_queries)
		conn.commit()

# Insert each row into toxins_raw table
# This methods inserts ALL values from csv to table
def insertToxinData(row):
	with conn.cursor() as cursor:
		sql = """
		INSERT INTO toxins_raw(year, county, municipality, facility, voc, nox, co, co2, particulate, pm10, pm25, haps, so2) 
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
		"""
		cursor.execute(sql, (
			row[0],
			row[1],
			row[2],
			row[4],
			row[6],
			row[7],
			row[8],
			row[9],
			row[10],
			row[11],
			row[12],
			row[13],
			row[14],
		))

# Loop over all of the rows in the toxin datasheet
# Load the data into the toxins_raw table
# The toxin_raw table will then be used to build an more refinied
# dataset in the toxins table, see the readme for more info
def loadToxinData():
	with open('datasets/Title_V_Emissions_Inventory__Beginning_2010.csv', 'r') as toxin_csv:
		reader = csv.reader(toxin_csv, delimiter=',')
		header = next(reader)

		# Load the raw table data into toxins_raw
		for row in reader:
			insertToxinData(row)

		# Average the raw data into toxins
		sql = """
		SELECT 
			county, 
			avg(voc) as voc, 
			avg(nox) as nox,
			avg(co) as co,
			avg(co2) as co2,
			avg(particulate) as particulate,
			avg(pm10) as pm10,
			avg(pm25) as pm25,
			avg(haps) as haps,
			avg(so2) as so2
		FROM toxins_raw 
		WHERE year >= 2012 
		AND year <= 2016 
		GROUP BY county;
		"""

		# Load the averages taken around the county into the average table
		with conn.cursor() as cursor:
			cursor.execute(sql, ())
			for row in cursor.fetchall():
				insertsql = "INSERT INTO toxins(county,voc,nox,co,co2,particulate,pm10,pm25,haps,so2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
				cursor.execute(insertsql, (
						row[0],
						row[1],
						row[2],
						row[3],
						row[4],
						row[5],
						row[6],
						row[7],
						row[8],
						row[9]
					))

			conn.commit();

# Insert a single row of cancer data
# Meant to abstract the insert and data purification process
def insertCancerData(row):
	with conn.cursor() as cursor:
		sql = """
		INSERT INTO cancers(county, cancer, cases, population, age_adjusted_rate) 
		VALUES (%s,%s,%s,%s,%s);
		"""

		if row[6] == "'Data Suppressed'":
			row[6] = "0";
		if row[5] == "'Data Suppressed'":
			row[5] = "0";
		if row[4] == "'Data Suppressed'":
			row[4] = "0";

		cursor.execute(sql, (
			row[1].replace(" County", "").upper().replace("'", ""),
			row[2].replace("'", ""),
			row[6].replace("'", ""),
			row[7].replace("'", ""),
			row[5].replace("'", ""),
		))

# Loop through the 3 cancer files and load them into the same database table
def loadCancerData():
	files = ["leukemias.csv","lung.csv","melanomas.csv"]
	for file in files:
		with open("datasets/" + file, "r") as cancer_csv:
			reader = csv.reader(cancer_csv, delimiter=',')
			header = next(reader)

			# Load the raw table data into toxins_raw
			for row in reader:
				insertCancerData(row)

			conn.commit();


def main():
	# TODO invoke your code to load the data into the database
	print("Building Database Schema...")
	buildSchema()
	print("Loading toxin data...")
	loadToxinData()
	print("Loading cancer data...")
	loadCancerData()
	print("Database Successfully Created and Data Loaded.")

if __name__ == "__main__":
	main()