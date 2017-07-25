import time

numOFboats = 10
costPerHour = 20
boatsIn = [True, True, True, True, True, True, True, True, True, True]
daysTake = 0

def main():
	que = input("\nIf you would like to hire a boat now type NOW, if you would \
like to book a boat for today type BOOK: ")
	times = time.localtime()
	if que.lower() == 'now':
		if times.tm_hour >= 10 and times.tm_hour < 18:
			booking(times)
		else:
			print("You can only hire between 10am and 5pm")
	else:
		print("Ok")
		main()

def booking(times):
	hour = times.tm_hour
	mins = times.tm_min
	print("\nHires are booked in 30 minute slots.\n")
	try:
		 time = float(input("How many hours would you like to hire boat for? \n"))
	except:
		print("Please Enter A Number.")
		booking()
	if time % 0.5 != 0:
		print("\nYou can only book in half an hour slots\n")
		booking()
	if time % 1 == 0:
		cost = time * costPerHour
	else:
		cost = (time - 0.5) * costPerHour + 12
	if mins >= 0 and mins <= 30:
		if time % 1 == 0:
			start = str(hour)+":30"
			end = str(hour+int(time))+":" + "30"
		else:
			start = str(hour)+":30"
			end = str(hour+int(time)+1)+":00"
		print("You are booked from %s to %s and that will cost $%i\n" %(start, \
			end, cost))
	if mins > 30 and mins <= 59:
		start = str(hour + 1)+":00"
		end = str(hour+int(time)+1)+":00"
		print("You are booked from %s to %s and that will cost $%i\n" %(start, \
			end, cost))


if __name__ == "__main__":
	main()