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