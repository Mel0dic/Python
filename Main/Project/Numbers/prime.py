# factors = lambda n: [x for x in range(1,n+1) if not n%x]
isPrime = lambda x,y: x + y
factors = lambda n: [x for x in range(1,n+1) if n%x]

def main():
	print(factors(10))
	print(10%5)
	s = [l for l in range(0, 10)]
	print(s)

if __name__ == "__main__":
	main()