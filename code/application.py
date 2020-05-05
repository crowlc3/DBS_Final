import os
from database import DatabaseController

def test():
	return

	


if __name__ == "__main__":
	print("Welcome to our application")
	print("Contributors: Christopher Pence, Howard Zhao, Aidan Duane, Caitlin Crowley")
	print("Please pick from one of these options to query our database:")
	arr = ["1: print all of the ____" , "2: print all of the _______" , "3: do this _____"]
	for item in arr:
		print(item)
	query = input("Enter the number of the query you would like to run: ")
	query_ = int(query)
	print("You selected",arr[query_-1])

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
# select data for apsecific type