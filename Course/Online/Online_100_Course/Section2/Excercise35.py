def main():
	string = input("Input a string: ")
	print(words(string))

def words(string):
	return len(string.split())

if __name__ == "__main__":
	main()