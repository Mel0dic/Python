def main():
	#Ask for input set given country find
	find = input("Enter a country: ")
	#Call Binary Search function with argument find
	BinarySearch(find)

#Define BinarySearch with argument that is being searched for
def BinarySearch(find):
	#Create countriesEU array filled with 12 countries from eu		
	countriesEu = ['Austria', 'Czech Republic', 'Denmark', 'France', 'Germany', 'Great Britain', 'Greece', 'Hungary',\
				  'Iceland', 'Ireland', 'Italy', 'Lithuania', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Spain', 'Sweden', 'Sweden', 'Switzerland']
	arraySize = len(countriesEu)
	#Set minNum to 0
	minNum = 0
	#Set maxNum to amount of elements in countriesEu -1
	maxNum = arraySize-1

	#While n is greater than 0
	while arraySize > 0:
		#Get halfway point of list, using int to make sure it isnt a float value	
		half = int((minNum + maxNum) / 2)
		#If country that is being looked for is at given halfway point
		if countriesEu[half] == find:
			#Print found message and return out of function	
			print("Found {} at point {}.".format(find, half))
			return
		#Else if value at the halfway point is less than the given country set the minimum value to the value after the halfway point 	
		elif countriesEu[half] < find:
			#Set the minimum value to the value after the halfway point 	
			minNum = half + 1
		#Else if the value at the halfway point is greater than the country being searched for
		else:
			#Set the maximum value to the value before the halfway point	
			maxNum = half-1
		#Recalculate the array size
		arraySize = maxNum - minNum + 1
	#Print country could not be found message	
	print("{} could not be found.".format(find))

if __name__ == "__main__":
	main()