import urllib2
url = "http://127.0.0.1:8082"

for i in range(5500, 5601):
	request = urllib2.request(url, headers=str(i))
	try:
		contents = urllib2.urlopen(request).read()
		print(contents)
	except:
		print(url)