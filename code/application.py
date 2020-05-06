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
import numpy
from texttable import Texttable
from database import DatabaseController

# Print database output in a nice table
def printTextTable(alignment, header, data):
	tt = Texttable(0)
	tt.set_max_width(0)
	tt.set_deco(Texttable.HEADER)
	tt.set_cols_align(alignment)
	tt.header(header)
	tt.add_rows(data, header=False)
	print()
	print(tt.draw())


def find_specific_cancer(db,type):
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.find_specific_cancer(type))

def high_low_comparison(db,type):
	printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l"],
					["County", "Min Cases", "Max Cases", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.high_low_comparison(type))

def cancer_cases_threshold(db):
	cases = input("How many cases would you like to set as the threshold? - ")
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.cancer_cases_threshold(cases))

def compare_cancer_rate_with_hl_toxin(db):
	cancer_type = pick_cancer()
	toxin_type = pick_toxin()
	printTextTable(["l","c","c","l"],
					["Cancer Type", "Cancer Rate", toxin_type + " Level", "County"],
					db.select_cancer_rate_with_hl_toxin(cancer_type, toxin_type))

def toxin_cancer_correlation(db,):
	cancer_type = pick_cancer()
	toxin_type = pick_toxin()
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
	print("\nThe correlation between " + cancer_type + " and " + toxin_type + " is: " + str(round(numpy.corrcoef(cancer_rate, toxin_level)[0][1], 4)))


def find_county_toxin_data(db):
	cancer_type = pick_cancer()
	county = input("Enter county name: ")
	printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l","l","l"],
					["County", "Cancer", "Cases","Population", "Age Adjusted Rate", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.find_county_toxin_data(county,cancer_type))



def pick_cancer():
	cancers = ["Leukemias", "Lung and Bronchus","Melanomas of the Skin"]
	for i in range(len(cancers)):
		print(i+1,"-",cancers[i])
	numby = input("Enter a cancer type: ")
	num = int(numby)
	return cancers[num-1]

def pick_toxin():
	toxins = ["voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"]
	for i in range(len(toxins)):
		print(i+1,"-",toxins[i])
	numby = input("Enter a toxin type: ")
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
	arr = ["1: find specific cancer",
			"2: highlow",
			"3: Correlation between toxin level and cancer rate over all counties.",
			"4: Compare cancer rates in counties with the highest and lowest levels of a given toxin.",
			"5: threshold cancer cases",
			"6: amount for a county"]


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
		elif query_ == 2:
			type = pick_cancer()
			high_low_comparison(db,type)
		elif query_ == 3:
			toxin_cancer_correlation(db)
		elif query_ == 4:
			compare_cancer_rate_with_hl_toxin(db)
		elif query_ == 5:
			cancer_cases_threshold(db)
		elif query_ ==6:
			find_county_toxin_data(db)


if __name__ == "__main__":
	main()