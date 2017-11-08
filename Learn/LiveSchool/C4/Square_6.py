def main():
	for i in range(2, 101):
		if isPrime(i):
			print("%2i is a prime number." % i)

def isPrime(query):
	for i in range(2, query):
		if query % i == 0:
			return False
	return True

if __name__ == "__main__":
	main()