#-------------Heres some ideas for queries-------------------#



# - At least two queries that select at least some data from both of your datasets

#*****Toxins*****
# Select the toxins levels per country
# Select the amount of a specific toxin in all counties

#*****Cancers*****
# Select the data from each type of cancer


# - At least two queries that showcase syntax beyond the basic `SELECT-FROM-WHERE` clauses (e.g., Grouping, Subqueries, etc.)

#*****Toxins*****
# Join Cancer on county

#*****Cancers*****
# Select the data with cases over a certain threshold


# - At least two queries that accept input entered by the user (as opposed to just allowing selection from a list of options)

#*****Toxins*****
# Select the amount of toxins for a specific county

#*****Cancers*****
# Select the data for a specific county
# select data for a specific type

import os
from texttable import Texttable
from database import DatabaseController

tt = Texttable(0)

# Print database output in a nice table
def printTextTable(alignment, header, data):
	global tt
	tt.set_deco(Texttable.HEADER)
	tt.set_cols_align(alignment)
	tt.header(header)
	tt.add_rows(data, header=False)
	print(tt.draw())
	tt.reset()


def find_specific_cancer(db,type):
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.find_specific_cancer(type))

def high_low_comparison(db,type):
	printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l","l","l"],
					["county", "cancer", "cancer" ,"cases", "cases", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.high_low_comparison(type))

def toxin_cancer_correlation(db):
	cancer_type = input("Select a type of cancer [Leukemias, Lung and Bronchus, Melanomas of the Skin]: ")
	toxin_type = input("Select a type of toxin []: ")
	data = db.select_toxin_cancer_correlation(cancer_type, toxin_type)

	printTextTable(["c", "c"],
					["Cancer Rate", "Toxin Level"],
					data)

	# Compute the correlation
	toxin_level = []
	cancer_rate = []
	for row in data:
		cancer_rate.append(row[0])
		toxin_level.append(row[1])
	print("The correlation between " + cancer_type + " and " + toxin_type + " is: " + str(numpy.corrcoef(toxin_level, cancer_rate)[0][1]))

def pick_cancer():
	cancers = ["Leukemias", "Lung and Bronchus","Melanomas of the Skin"]
	for i in range(len(cancers)):
		print(i+1,"-",cancers[i])
	numby = input("Enter the number for which cancer you would like to get information on: ")
	num = int(numby)
	return cancers[num-1]

def pick_toxin():
	toxins = ["voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"]
	for i in range(len(toxins)):
		print(i+1,"-",toxins[i])
	numby = input("Enter the number for which toxin you would like to get information on: ")
	num = int(numby)
	return toxins[num-1]

def main():
	# Initialize Imports
	db = DatabaseController()

	# Begin text interaction with user
	print("\nWelcome to our application")
	print("Contributors: Christopher Pence, Howard Zhao, Aidan Duane, Caitlin Crowley")
	print()
	print("Enter q to quit\n")


	#array of options for queries
	arr = ["1: find specific cancer","2: highlow"]


	query = 's'


	while(query != 'q'):
		print("\nPlease pick from one of these options to query our database:\n")

		for item in arr:
			print(item)
			###Print options

		query = input("Enter the number of the query you would like to run: ")

		if(query == 'q'):
			print("Bye Bye\n")
			break
			###End program

		query_ = int(query)


		print("You selected",arr[query_-1])

		#run function per user input
		if query_ == 1:
			type = pick_cancer()
			find_specific_cancer(db,type)
		if query_ == 2:
			type = pick_cancer()
			high_low_comparison(db,type)


if __name__ == "__main__":
	main()