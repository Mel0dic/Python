import sys
import time

row = 10
column = 10

for i in range(row):
	for x in range(column):
		sys.stdout.write("\r{0}>".format("="*i))
		sys.stdout.flush()
		time.sleep(0.1)
	print("")