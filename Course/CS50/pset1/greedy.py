def main():
	one = five = ten = twentyfive = 0
	changed = input("How much change is owed? ")

	print("$%.2f" %(float(changed)))
	change = float(changed)

	while change > 0.0099999999999999999999999999:
		#print(change)
		if change > 0.2500:
			twentyfive +=1
			change -= 0.25
		elif change > 0.10:
			ten += 1
			change -= 0.10
		elif change > 0.05:
			five += 1
			change -= 0.05
		elif change > 0.01:
			one += 1
			change -= 0.01
	print("%i 25p Coins" %(twentyfive))
	print("%i 10p Coins" %(ten))
	print("%i 5p Coins" %(five))
	print("%i 1p Coins" %(one))

main()