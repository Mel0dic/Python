import string

for i in string.ascii_lowercase:
	with open(i+".txt", "w") as file:
		file.write(i)
		print(i)