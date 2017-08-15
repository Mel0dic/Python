a = [1, 2, 3]
b = (4, 5, 6)

zipped = zip(a, b)

zipp = list(zipped)

print(zipp[0][0] + zipp[0][1])
print(zipp[1][0] + zipp[1][1])
print(zipp[2][0] + zipp[2][1])

"""
THE AWNSER
"""

for i, j in zip(a, b):
	print(i + j)
