import re

# Hard Way

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != "-":
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != "-":
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

message = u'Call 415-555-1011 else 424-111-1111'
foundNumber = False
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print(chunk)
		foundNumber = True
if not foundNumber:
	print(False)

# Easy Way

phoneNumRegX = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegX.search(message)
print(mo.group())

mo = phoneNumRegX.findall(message)
print(mo)