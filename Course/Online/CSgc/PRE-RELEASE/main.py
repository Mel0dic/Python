#Inistalize and declare starting data for boatInfo [is boat in?, max hire length, time hired]
boatInfo = [[True, 0, 0], [True, 0, 0], [True, 0, 0], [True, 0, 0], [True, 0, 0], \
[True, 0, 0], [True, 0, 0], [True, 0, 0], [True, 0, 0], [True, 0, 0],]

#The cost the boat isto hire for an hour
costPerHour = 20

#The running total of the take through the day
dayTake = 0.00

def Main():

	global dayTake

	#Set continue to "y" to allow for a sort of do while loop
	continueYN = "y"

	while continueYN.lower() == "y":

		#Call Function Boat Length And set return value to hireLength
		hireLength = boatLength()

		#Call function costCalc with value hireLength
		dayTakeTemp, continueYN = costCalc(hireLength)

		#Add the cost of the ride to the running total for the day.
		dayTake += dayTakeTemp

	#DEBUG
	for i in boatInfo:
		print(i)

#Define function boatLength to get how long you would like to hire boat for
def boatLength():
	#Ask for and take input and set it equal to hireLength
	hireLength = float(input("How many hours would you like to hire a boat for? Ex 1.5:  "))

	#Check if input is valid, if not valid ask for another input
	if hireLength % 0.5 != 0:
		print("You are only allowed 1 or .5 hour slots")
		boatLength()

	#Return input hireLength
	return hireLength

#Define function costCalc to calculate the cost
def costCalc(hireLength):
	#Get start time set it to startTime
	startTime = int(input("What time would you like to start? Ex 1230:  "))

	#Check if start time is < 10:00 if it is call itself to input a new time
	if startTime < 1000:
		print("We only allow you to hire from 10am")
		return costCalc(hireLength)

	#if start time has a .5 hour slot and if startTime % 100 is an int
	if hireLength % 1 == 0 and isinstance(startTime % 100, int):
		#Add hireLength x 100 to startTime set as returnTime
		returnTime = startTime + hireLength * 100
	else:
		#If start time starts at half past and hire length is half hour
		if int(startTime % 100) == 30 and hireLength - int(hireLength) != 0:
			#
			returnTime = (startTime - 30) + ((hireLength - 0.5) * 100) + 100
		#Else if start time is on the hour or hire length is either an hour or half hour
		else:
			returnTime = (startTime + (hireLength * 100)) + 30

	#Check if start time is past closing time 
	if returnTime > 1700:
		print("You cannot hire a boat past 17:00")
		Main()
	else:
		#If return time is not on a half hour slot
		if returnTime % 100 == 0:
			print("The boat must be returned by " + str(int(returnTime / 100)) + ":00")
		else:
			#if return time is greater than 60
			if returnTime % 100 > 60:
				#return time = (returnTime - 30 / 100) + 1 * 100 + returnTime % 100 - 50
				returnTime = ((int((returnTime - 30) / 100) + 1) * 100) + (int(returnTime % 100) - 50)
				print("The boat must be returned by " + (str(int(returnTime/100)) + ":" + str(returnTime % 100)))
			else:
				returnTime = (int((returnTime - 30) / 100) + 1) * 100 + (int(returnTime % 100))
				print("The boat must be returned by " + (str(int(returnTime/100)) + ":" + str(returnTime % 100)))

	yesOrNo = boatHire(returnTime, hireLength)

	#Check if hire length has half hour slots to calculate cost and add to dayTake
	if hireLength % 1 == 0:
		cost = hireLength * costPerHour
		return cost, yesOrNo
	else:
		cost = ((hireLength - 0.5) * costPerHour) + 12
		return cost, yesOrNo

#Define boatHire to hire out single boat from fleet of 10
def boatHire(returnTime, hireLength):

	reportYN = input("Would you like to print a report? Y/N:  ")

	while reportYN.lower() not in ('y', 'n'):
		 	print(reportYN)
		 	reportYN = input("Would you like to print a report? Y/N:  ")

	lowest = 1700

	#Loop throogh boat array for first one available and set it to away
	for boat in boatInfo:
		if boat[0] == False:
			if boat[1] < lowest and boat[1] != 0:
				lowest = boat[1]
			continue
		else:
			boat[0], boat[1] = False, returnTime
			boat[2] += hireLength
			toReturn = boat
			break
	if reportYN.lower() == 'y':
		for boat in range(0, len(boatInfo)):
			print("Boat {0} was {1}".format(boat + 1, ("not hired" if boatInfo[boat][0] and boatInfo[boat][2] == 0 else "hired")))

	yesOrNo = input("Would you like to hire another boat? (Y/N)")

	while yesOrNo.lower() not in ('y', 'n'):
		yesOrNo = input("Would you like to hire another boat? (Y/N)")
		print("Invalid Input")

	if yesOrNo.lower() == 'y':
		return 'y'
	else:
		return 'n'

Main()