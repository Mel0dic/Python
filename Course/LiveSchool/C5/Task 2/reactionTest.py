import winsound, random, time

frequency = 1500  # Set Frequency To 1500 Hertz
duration = 50  # Set Duration To 100 ms == .1 second

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

	#Beep for .1 seconds at 1500 Hertz	
	winsound.Beep(frequency, duration)
	#Record time
	startTime = time.time()
	#Wait for an input
	x = str(input("GO: "))
	#Taks the start time from the cureent time and print the difference	
	print("Your time was: {}".format(time.time() - startTime))

	#If the input was not just enter break out of the loop
	if x != "":
		break