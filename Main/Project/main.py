import pyspeedtest

def main():
	test = pyspeedtest.SpeedTest()
	print("%.2fMbps" %(test.download()/1000000))
	return

if __name__ == "__main__":
	main()