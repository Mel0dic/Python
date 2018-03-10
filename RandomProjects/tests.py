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


