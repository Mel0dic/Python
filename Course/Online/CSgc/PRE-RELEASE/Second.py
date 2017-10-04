boatInfo = [True]
costPerHour = 20

def Main():

	dayTake = 0.00

	#Call Function Boat Length And set return value to hireLength
	hireLength = boatLength()

	#Call function costCalc with value hireLength
	dayTake += costCalc(hireLength)

	print(dayTake)

#Defin function boatLength to get how long you would like to hire boat for
def boatLength():
	#Ask for and take input and set it equal to hireLength
	hireLength = float(input("How many hours would you like to hire a boat for? Ex 1.5 "))

	#Check if input is valid, if not valid ask for another input
	if hireLength % 0.5 != 0:
		print("You are only allowed 1 or .5 hour slots")
		boatLength()
 
	#Return input hireLength
	return hireLength

#Define function costCalc to calculate the cost
def costCalc(hireLength):
	#Get start time set it to startTime
	startTime = int(input("What time would you like to start? Ex 1230 "))

	if startTime < 1000:
		print("We only allow you to hire from 10am")
		return costCalc(hireLength)

	if hireLength % 1 == 0 and isinstance(startTime % 100, int):
		returnTime = startTime + hireLength * 100
	else:
		if int(startTime % 100) == 30 and hireLength - int(hireLength) != 0:
			returnTime = (startTime - 30) + ((hireLength - 0.5) * 100) + 100
			print(returnTime)
		else:
			returnTime = (startTime + (hireLength * 100)) + 30

	#Check if start time is past closing time 
	if returnTime > 1700:
		print("You cannot hire a boat past 17:00")
		Main()
	else:
		print(returnTime)
		if returnTime % 100 == 0:
			print("The boat must be returned by " + str(int(returnTime / 100)) + ":00")
		else:
			if returnTime % 100 > 60:
				print("The boat must be returned by " + str(int((returnTime - 30) / 100) + 1) + ":" + str(int(returnTime % 100) - 50))
			else:
				print("The boat must be returned by " + str(int((returnTime - 30) / 100) + 1) + ":" + str(int(returnTime % 100)))

	#Check if hire length has half hour slots to calculate cost and add to dayTake
	if hireLength % 1 == 0:
		cost = hireLength * costPerHour
		print(str(hireLength) + " * " + str(costPerHour) + " = " + str(hireLength * costPerHour))
		return cost
	else:
		cost = ((hireLength - 0.5) * costPerHour) + 12
		print(str(hireLength) + "- 30 * " + str(costPerHour) + " = " + str((hireLength - 30) * costPerHour) + " + 12" + str((hireLength - 30) * costPerHour + 12))
		return cost

#Define boatHire to hire out single boat from fleet of 10
def boatHire():
	#Loop throogh boat array for first one available and set it to away
	for boat in boatInfo:
		if boat[0] == False:
			continue
		else:
			boat[0] = False
			break	

Main()