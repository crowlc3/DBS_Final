retrive_data.py Notes and Instructions:
	
	When retriving the data you want to verify that 4 files are downloaded under the following names:
		leukemias.csv
		lung.csv
		melanomas.csv
		Title_V_Emissions_Inventory__Beginning_2010.csv

	The first three files listed above are not downloading from their original source. The original link found in our proposal creates temporary download links from dynamic user options entered on this page. This rendered it impossible to ensure retrieve_data.py could download from their site. So we downloaded the three files manually and are hosting them on Chris's webserver. (The downloads were also 'blob:' types which did not play nice with the code in retrieve_data.py.)

load_data.py Notes and Instructions:
	
	load_data.py will directly attempt to access the files above by their names above. This is why it is important that the file names are exactly as listed above. 

	This process will load the first three cancer data files into one table and the emissions file into another. Please see additional notes on this below.

toxins_raw vs toxins:



SQL injection prevention:
