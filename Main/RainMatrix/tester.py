import sys, time, random, os

row, column = os.get_terminal_size()

letters = ["0", "1", " "]
stringLine = ""

for i in range(column):
	for x in range(row):
		stringLine += (letters[random.randint(0, 2)])
	#stringLine += (" "*column)*row
	sys.stdout.write("\r{0}".format(stringLine))
	sys.stdout.flush()
	stringLine = ""
	time.sleep(0.1)