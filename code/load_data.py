import psycopg2

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password' port=5433"

# TODO add your code here (or in other files, at your discretion) to load the data
conn = psycopg2.connect(connection_string)

# Build the schema based on the schema file
def buildSchema():
    with conn.cursor() as cursor:
        setup_queries = open('schema.sql', 'r').read()
        cursor.execute(setup_queries)
        conn.commit()

# Load data from the sources into the database
def loadData():
	with conn.cursor() as cursor:
		print("TODO")


def main():
    # TODO invoke your code to load the data into the database
    print("Building Database Schema...")
    buildSchema()
    print("Loading Data From Sources...")
    loadData()


if __name__ == "__main__":
    main()
