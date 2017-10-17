import time, random
from threading import Thread



#Declare Dictionary Vaiable
messageTime = {}

#Word list
wordList = ["Hello", "Hi", "Goodbye", "Message", "This", "Is", "Random"]

def main():
	for i in range(10):
		t = Thread(target=myFunc, args=(i,))
		t.start()

	time.sleep(11)

	print("")

	#Random or given message choices
	choice = input("Enter 1 for random generation, enter 2 to input message: ")

	#If 1 was entered generate random time and message
	if choice == "1":
		#For number in random range (random amount of messages generated)
		for i in range(random.randint(2, 10)):
			tempMessage = ""
			#Random number for amount of words in message
			for word in range(random.randint(3, 7)):
				#Add word to current message
				tempMessage = " ".join((tempMessage, wordList[random.randint(0, len(wordList)-1)]))
			#Generate a random time
			tempTime = random.randint(1, 10)
			#Add word and time to dictionary
			messageTime[tempMessage] = tempTime
	elif choice == "2":
		#Enter message function
		enterMessages()
	else:
		#If neither 1 or 2 was entered exit
		exit()

	#For item in dictionary pass word and time into messageFunc function and start thread
	for i in messageTime:
		t = Thread(target=messageFunc, args=(i, messageTime[i],))
		t.start()



def myFunc(i):
	print("\nSleeping {} sec from thread {}".format((i+1), i))
	time.sleep(i+1)
	print("\nfinished sleeping from thread %d" % i)



def messageFunc(message, timing):
	#Take time and sleep
	time.sleep(timing)
	#Print new line then message
	print("\n{}".format(message))



def enterMessages():
	while 1:
		#Get message
		tempMessage = input("\nEnter A Message: ")
		while 1:
			#Get time
			tempTime = input("Enter A Time: ")
			#Try to convert time into an int if returns an error ... ask for input again
			try:
				tempTime = int(tempTime)
				break
			except ValueError:
				print("Please enter an integer: ")

		#Append the dictionary with the message and time
		messageTime[tempMessage] = tempTime

		#Ask if user would like to continue
		new = input("Input Y to enter another message: ")

		#If user woould like to continue call same function
		if new.lower() != "y":
			break



if __name__ == "__main__":
	main()