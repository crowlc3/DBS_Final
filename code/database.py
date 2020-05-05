import psycopg2
import os

class DatabaseController:

	def __init__(self):
		db_port = os.getenv('db_port') or '5432';
		connection_string = "host='localhost' \
							dbname='dbms_final_project' \
							user='dbms_project_user' \
							password='dbms_password' \
							port=" + db_port;
		self.conn = psycopg2.connect(connection_string)

	# Private method to abstract running query
	def __runQuery(self, query, params=()):
		with self.conn.cursor() as cursor:
			cursor.execute(query, params)
			return cursor.fetchall()

	def find_specific_cancer(self,cancer_type):
		query = "SELECT * FROM cancers WHERE CANCER LIKE %s;"
		return self.__runQuery(query,[cancer_type])



def main():
	print("This class should not be run on it's own.")

if __name__ == "__main__":
	main()