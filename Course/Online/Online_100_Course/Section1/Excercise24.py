d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# print("b has value " + str(d['b']))
# print("c has value " + str(d['c']))
# print("a has value " + str(d['a']))

#My Awnser
for i in d.items():
	print("%s has value %s" %(i[0], i[1]))

print("\n The Awnser \n")

#The Awnser
for key, value in d.items():
	print("%s has value %s" %(key, value))
