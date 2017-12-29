#http://usingpython.com/python-programming-challenges/

nameStore = input("Enter your full name: ")

length = 6
BannerTopBot = ""

for i in nameStore:
	length += 1

for i in range(0, length):
	BannerTopBot += "-"

print(BannerTopBot)
print(".::" + nameStore + "::.")
print(BannerTopBot)

