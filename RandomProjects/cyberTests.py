<<<<<<< HEAD
from zipfile import ZipFile

for i in range(100, 1000):
	with ZipFile('/tmp/alien-zip-2092.zip') as zf:
		try:
			zf.extractall(pwd=str(i))
			print i
			break
		except IOError:
			print i
			pass


for i in possiblePasswordList:
	try:
		zf = ZipFile.open('/tmp/alien-sample-42.zip', 'r', pwd=i)
		print i
		zf.extractall()
		break
	except:
		pass




import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("localhost", 10000) )
s.send("GET_KEY")
recv = s.recv(1024)
print recv

recv = recv[::-1]

print recv

s.send(recv)

s.close



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("localhost", 10000) )
s.send("/tmp")
s.send("all")
recv = s.recv(1024)
print recv
s.close




import magic


=======
import urllib2
url = "http://127.0.0.1:8082"

for i in range(5500, 5601):
	request = urllib2.request(url, headers=str(i))
	try:
		contents = urllib2.urlopen(request).read()
		print(contents)
	except:
		print(url)



from zipfile import ZipFile

for pwd in range(0, 999):
	try:
		mainZF = zipfile("/tmp/alien-zip-2092.zip", "r")
		mainZF.open("alien-zip-2092", "r")
		print pwd
		exit()
	except IOError:
		print "Error"

from zipfile import ZipFile

for i in range(0, 1000):
	try:
		with ZipFile("/tmp/alien-zip-2092.zip") as zf:
			zf.extractall(path="/tmp",pwd=str(i))
			with open("/tmp/alien-zip-2092.txt", "r") as textFile:
				for line in textFile:
					print line
			print i
			exit()
	except RuntimeError:
		zf.close()




import urllib2
url = "http://127.0.0.1:8082"

#request = urllib2.open(url)

reque = urllib2.Request(url, "GET /")

r2 = urllib2.urlopen(reque)
print r2.read()
