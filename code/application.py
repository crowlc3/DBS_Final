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

tt = Texttable()

# Print database output in a nice table
def printTextTable(alignment, header, data):
	global tt
	tt.set_deco(Texttable.HEADER)
	tt.set_cols_align(alignment)
	tt.header(header)
	tt.add_rows(data, header=False)
	print(tt.draw())
	tt.reset()

def find_specific_cancer(db,tt):
	type = input("Type which cancer you want to get data for [Leukemias, Lung and Bronchus, Melanomas of the Skin]: ")
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.find_specific_cancer(type))

def main():
	# Initialize Imports
	db = DatabaseController()

	# Begin text interaction with user
	print("Welcome to our application")
	print("Contributors: Christopher Pence, Howard Zhao, Aidan Duane, Caitlin Crowley")
	print("Please pick from one of these options to query our database:")


	#array of options for queries
	arr = ["1: find specific cancer"]


	query = 's'


	while(query != 'q'):
		print()
		print()
		for item in arr:
			print(item)
		query = input("Enter the number of the query you would like to run: ")
		if(query == 'q'):
			print("Bye Bye\n")
			break
		query_ = int(query)


		print("You selected",arr[query_-1])

		#run function per user input
		if query_ == 1:
			find_specific_cancer(db,tt)


if __name__ == "__main__":
	main()