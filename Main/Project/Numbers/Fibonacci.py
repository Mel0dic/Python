#Enter a number and have the program generate 
#the Fibonacci sequence to that number or to the Nth number.

def main():
	fibonacci(int(input("Enter The Length Of The Number: ")))
	for i in arr:
		print(str(i), end='')
		if i != arr[len(arr)-1]:
			print(", ", end='')
	print("")

arr = [0, 1]

def fibonacci(n, s=1):
	arr.append(arr[s]+arr[s-1])
	if len(arr) == n:
		return
	fibonacci(n, s+1)

if __name__ == "__main__":
	main()