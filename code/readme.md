Video:
	https://drive.google.com/file/d/1xSw1Yzt_2DFfp6OzxUpkYEcM3zQB6QDk/view?usp=sharing

retrive_data.py Notes and Instructions:
	
	When retriving the data you want to verify that 4 files are downloaded under the following names:
		leukemias.csv
		lung.csv
		melanomas.csv
		Title_V_Emissions_Inventory__Beginning_2010.csv

	The first three files listed above are not downloading from their original source. The original link found in our proposal creates temporary download links from dynamic user options entered on this page. This rendered it impossible to ensure retrieve_data.py could download from their site. So we downloaded the three files manually and are hosting them on Chris's webserver. (The downloads were also 'blob:' types which did not play nice with the code in retrieve_data.py.)

load_data.py Notes and Instructions:
	
	load_data.py will directly attempt to access the files above by their names above. This is why it is important that the file names are EXACTLY as listed above. 

	This process will load the first three cancer data files into one table and the emissions file into another. Please see additional notes on this below.

toxins_raw vs toxins:
	Data from 'Title_V_Emissions_Inventory__Beginning_2010.csv' initially gets loaded into the toxins_raw table. This transition moves all of the data from the CSV to the database in the exact same column structure. The toxin data is too granular for the rest of our queries so instead of combining rows in each query we run, we do this all at the start and move the combined data to the toxins table.

	toxins_raw granularity:
		County -> Municipality -> Facility

	toxins granularity:
		County

	cancer granularity:
		County

	What we do is average the data provided in the extra rows into a single row for each county. That is the data that exists in the toxin table. All of this occurs in the load_data.py file.

SQL injection prevention:
	We use two methods to prevent SQL injection in our code.

	1. We know that there are 3 types of cancer and 9 types of emissions. Therefore, we have users select from a pre-determined list and insert that pre-determined value into the query. No direct user input has access to the query with this method.

	2. The second method is the normal parameters input in the execute command like discussed in class. This is used when a user provides a county that they would like to filter for. We didn't take the time to pre-set the counties so their direct input makes it into the database.