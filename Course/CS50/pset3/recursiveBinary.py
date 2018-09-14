def main():
	testArray = [1, 2, 3, 4, 5]
	search(testArray, 3)


def search(arr, target):
	mid = int((0 + len(arr)) / 2)
	if arr[mid] == target:	return True


if __name__ == "__main__":
	main()