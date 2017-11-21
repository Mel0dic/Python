def main():
	#Ask for input set given country find
	find = input("Enter a country: ")
	LinierSearch(find)

# def LinierSearch(find):
# 	countriesEu = ["Great Britain", "France", "Iceland", "Ireland", "Italy", "San Marino", "Serbia", "Slovakia", "Spain", "Sweden", "Switzerland", "Germany"]
# 	pointer = 0 
# 	while pointer < len(countriesEu) and countriesEu[pointer] != find:
# 		pointer += 1
# 		if countriesEu[pointer] == find:
# 			print("Found {} at point {}.".format(find, (pointer + 1)))
# 	print("{} could not be found.".format(find))

#Define LinierSearch with argument that is being searched for
def LinierSearch(find):
	#Create countriesEU array filled with 12 countries from eu		
	countriesEu = ["Great Britain", "France", "Iceland", "Ireland", "Italy", "San Marino", "Serbia", "Slovakia", "Spain", "Sweden", "Switzerland", "Germany"]
	#For every element in countriesEu	
	for i in countriesEu:
		#If element is == to the one being looked for
		if i == find:
			#Print found message and return out of function	
			print("Found {} at point {}.".format(i, i))
			return
	#If its been through every element and can't find the one being looked for print could not be found message
	print("{} could not be found.".format(find))



if __name__ == "__main__":
	main()