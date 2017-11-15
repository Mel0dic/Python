import winsound, random, time

frequency = 2000  # Set Frequency To 2000 Hertz
duration = 100  # Set Duration To 100 ms == .1 second

x = ""

#Create an infinite loop
while 1:
	print("When the beep sounds and the GO message prints press ENTER or type anything else to exit")
	#For loop that loops backwards from a random range between 3, 6
	for i in range(random.randrange(3, 6), 0, -1):
		print("The program will start in {}".format(i))
		#Sleep the program for 1 second	
		time.sleep(1)

	#Sleep the program for a random time between 2 and 10 seconds
	time.sleep(random.randrange(2, 10))

	#Beep for .1 seconds at 2000 Hertz	
	winsound.Beep(frequency, duration)
	#Record time
	startTime = time.time()
	#Wait for an input
	x = str(input("GO: "))
	#Record time after input
	endTime = time.time()
	#Taks the second time from the second time and print the difference	
	print(endTime - startTime)

	#If the input was not just enter break out of the loop
	if x != "":
		break