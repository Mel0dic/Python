import InsertionSort, BubbleSort, NumberGenerator, time

def main():
	for i in [10, 100, 1000, 10000]:
		print("Bubble Sort took {} seconds with a list of length {}".format(bubbleTimer(NumberGenerator.arrayGenerator(i))[0], i))
		print("Insertion Sort took {} seconds with a list of length {}".format(insertionTimer(NumberGenerator.arrayGenerator(i))[0], i))

#define bubbleTime function with the list as an argument
def bubbleTimer(alist):
	#Assign variable start time with time before we start
	startTime = time.time()
	#Call function bubble sort with list
	sortedList = BubbleSort.bubbleSort(alist)
	#Return current time - time at start to get the amount of time inbetween and the sorted list
	return (time.time() - startTime), sortedList

#define insertionTimer function with the list as an argument
def insertionTimer(alist):
	#Assign variable start time with time before we start
	startTime = time.time()
	#Call function bubble sort with list
	sortedList = InsertionSort.insertionSort(alist)
	#Return current time - time at start to get the amount of time inbetween and the sorted list
	return (time.time() - startTime), sortedList

if __name__ == "__main__":
	main()