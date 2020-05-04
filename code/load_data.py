import psycopg2
import csv

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password' port=5433"

# TODO add your code here (or in other files, at your discretion) to load the data
conn = psycopg2.connect(connection_string)

# Build the schema based on the schema file
def buildSchema():
	with conn.cursor() as cursor:
		setup_queries = open('schema.sql', 'r').read()
		cursor.execute(setup_queries)
		conn.commit()

# Insert each row into toxin table
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
def loadToxinData():
	with open('datasets/Title_V_Emissions_Inventory__Beginning_2010.csv', 'r') as toxin_csv:
		reader = csv.reader(toxin_csv, delimiter=',')
		header = next(reader)

		# Load the raw table data into toxins_raw
		for row in reader:
			insertToxinData(row)

		# Average the raw data into toxins_avg
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
				insertsql = "INSERT INTO toxins_avg(county,voc,nox,co,co2,particulate,pm10,pm25,haps,so2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
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

def main():
	# TODO invoke your code to load the data into the database
	print("Building Database Schema...")
	buildSchema()
	print("Loading toxin data...")
	loadToxinData()


if __name__ == "__main__":
	main()
