import os
import numpy
import matplotlib
import matplotlib.pyplot as plt
from texttable import Texttable
from database import DatabaseController

matplotlib.style.use('seaborn-bright')

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

def find_specific_cancer(db):
	type = pick_cancer()
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.find_specific_cancer(type))

def toxin_cancer_correlation(db):
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
	correlation = round(numpy.corrcoef(cancer_rate, toxin_level)[0][1], 4)
	print("\nThe correlation between " + cancer_type + " and " + toxin_type + " is: " + str(correlation))

	# Output scatterplot
	plt.scatter(cancer_rate, toxin_level)
	plt.xlabel(cancer_type + " Cancer Rate")
	plt.ylabel(toxin_type + " Level (Tons)")
	plt.title("Correlation = " + str(correlation))
	plt.savefig("plots/scatterplot.png")
	plt.clf()
	print("\nA scatterplot of this data has been saved under plots/scatterplot.png")

def county_cases_totaled(db):
	county_name = input("Enter county name: ")
	printTextTable(["l","c","c","c"],
					["County", "Total Cases", "Population", "Cancer Rate %"],
					db.select_county_cases_totaled(county_name))

def compare_cancer_rate_with_hl_toxin(db):
	cancer_type = pick_cancer()
	toxin_type = pick_toxin()
	printTextTable(["l","c","c","l"],
					["Cancer Type", "Cancer Rate %", toxin_type + " Level", "County"],
					db.select_cancer_rate_with_hl_toxin(cancer_type, toxin_type))

def high_low_case_comparison(db):
	type = pick_cancer()
	printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l"],
					["County", "Min Cases", "Max Cases", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.high_low_case_comparison(type))

def toxins_in_all_counties(db):
	printTextTable(["l","l","l","l","l","l","l","l","l","l"],
					["County", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.toxins_in_all_counties())

def select_specific_toxin(db):
	toxin = pick_toxin()
	printTextTable(["l","l"],
					["County", toxin],
					db.select_specific_toxin(toxin))

def cancer_cases_threshold(db):
	cases = input("How many cases would you like to set as the threshold? - ")
	printTextTable(["l","l","l","l","l"],
					["County", "Cancer", "Cases", "Population", "Age Adjusted Rate"],
					db.cancer_cases_threshold(cases))

def find_county_toxin_data_with_cancer(db):
	cancer_type = pick_cancer()
	county = input("Enter county name: ")
	printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l","l","l"],
					["County", "Cancer", "Cases","Population", "Age Adjusted Rate", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.find_county_toxin_data_with_cancer(county,cancer_type))

def find_county_toxin_data(db):
	county = input("Enter county name: ")
	printTextTable(["l","l","l","l","l","l","l","l","l","l"],
					["County", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
					db.find_county_toxin_data(county))

def toxins_threshold(db):
	toxin = pick_toxin()
	threshold = input("Etner threshold: ");
	printTextTable(["l","l"],
					["County", toxin],
					db.toxins_threshold(toxin,threshold))

def toxins_and_cancers(db):
    printTextTable(["l","l","l","l","l","l","l","l","l","l","l","l","l","l"],
                    ["County", "Cancer", "Cases","Population", "Age Adjusted Rate", "voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"],
                    db.toxins_and_cancers())

def pick_cancer():
	print()
	cancers = ["Leukemias", "Lung and Bronchus","Melanomas of the Skin"]
	for i in range(len(cancers)):
		print(i+1,"-",cancers[i])
	numby = input("Enter a cancer type: ")
	num = int(numby)
	return cancers[num-1]

def pick_toxin():
	print()
	toxins = ["voc: Volatile Organic Compounds",
			"nox: Nitrogen Dioxide and Nitric Oxide",
			"co: Carbon Monoxide",
			"co2: Carbon Dioxide",
			"particulate: Contaminants Suspended in Air",
			"pm10: Particulate Matter (10 micrometers or less in diameter)",
			"pm25: Particulate Matter (2.5 micrometers or less in diameter)",
			"haps: Hazardous Air Pollutants",
			"so2: Sulfur Dioxide"]
	toxins_ = ["voc", "nox", "co", "co2", "particulate", "pm10", "pm25", "haps", "so2"]
	for i in range(len(toxins)):
		print(i+1,"-",toxins[i])
	numby = input("Enter an emission type: ")
	num = int(numby)
	return toxins_[num-1]

def main():
	# Initialize Imports
	db = DatabaseController()

	# Begin text interaction with user
	print("\nWelcome to our application")
	print("Contributors: Christopher Pence, Howard Zhao, Aidan Duane, Caitlin Crowley")
	print()
	print("Enter q to quit\n")

	main_choices = ["1: Cancer Information Only", "2: Emission Information Only", "3: Both"]

	cancer = ["1: Find information on a specific type of cancer",
			"2: Find amount of cases over a certain threshold",
			"3: Find totaled amount of cases for a county"]

	emission = ["1: Find emission information for a certain county",
			"2: Find emission information for all counties",
			"3: Find amount of emissions over a certain threshold",
			"4: Find all emission information for a specific emission"]

	both = ["1: View all information",
			"2: Find emission cancer correlation",
			"3: Compare information for highest amount of cases and lowest amount of cases",
			"4: Find county specific data with cancer",
			"5: Compare cancer rates in counties with the highest and lowest levels of a given emission."]


	query = 's'


	while(query != 'q'):
		print("\nPlease pick from one of these options to query our database:\n")

		for item in main_choices:
			print(item)
			###Print options


		query = input("Enter the number of the data you want to query: ")

		if(query == 'q'):
			print("Bye Bye\n")
			break
			###End program

		query_ = int(query)

		if(query_==1):
			#cancer info only
			print()
			for item in cancer:
				print(item)
			queryc = input("Enter the number of the query you would like to run: ")

			if(queryc == 'q'):
				print("Bye Bye\n")
				break
				###End program

			query_c = int(queryc)

			if(query_c == 1):
				find_specific_cancer(db)
			elif(query_c == 2):
				cancer_cases_threshold(db)
			elif(query_c == 3):
				county_cases_totaled(db)

		elif(query_==2):
			#toxin info only
			print()
			for item in emission:
				print(item)
			queryt = input("Enter the number of the query you would like to run: ")

			if(queryt == 'q'):
				print("Bye Bye\n")
				break
				###End program

			query_t = int(queryt)

			if(query_t==1):
				find_county_toxin_data(db)
			elif(query_t==2):
				toxins_in_all_counties(db)
			elif(query_t==3):
				toxins_threshold(db)
			elif(query_t==4):
				select_specific_toxin(db)

		elif(query_==3):
			#both
			print()
			for item in both:
				print(item)
			queryb = input("Enter the number of the query you would like to run: ")

			if(queryb == 'q'):
				print("Bye Bye\n")
				break
				###End program

			query_b = int(queryb)

			if(query_b==1):
				toxins_and_cancers(db)
			elif(query_b==2):
				toxin_cancer_correlation(db)
			elif(query_b==3):
				high_low_case_comparison(db)
			elif(query_b==4):
				find_county_toxin_data_with_cancer(db)
			elif(query_b == 5):
				compare_cancer_rate_with_hl_toxin(db)


if __name__ == "__main__":
	main()