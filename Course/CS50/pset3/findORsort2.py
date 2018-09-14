'''
Search and a sort algorithm
'''
import numpy

def main():
	arrayOfNumbs = [12, 10, 5, 14, 3, 12, 9, 8, 7, 5, 13]
	sortednumbs = sort(arrayOfNumbs, len(arrayOfNumbs))
	print(search(3, sortednumbs, len(arrayOfNumbs)))


#Binary Search
#Search algorithm requires value to be sorted in size order
#Define search with target value list of numbers and size of array
def search(target, values, n):
	#If length of array less than 0 return False
	if n < 0:
		return False
	#Set minNum to 0
	minNum = 0
	#Set maxNum to n-1
	maxNum = n-1

	#While n is greater than 0
	while n > 0:
		half = int((minNum + maxNum) / 2)
		if values[half] == target:
			return True
		elif values[half] < target:
			minNum = half + 1
		else:
			maxNum = half-1
		n = maxNum - minNum + 1
	return False


#Sort 
#Define a number sorting algorithm with array of values and n length of array or use .sort
#you know who cares
def sort(values, n):
	counter = numpy.zeros(65536)

	for i in range(0, n):
		counter[values[i]] += 1

	for i in range(65536):
		if counter[i] > 0:
			for i in range(0, counter[i]):
				values[que] = i
				que += 1

if __name__ == "__main__":
	main()