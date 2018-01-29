import json
from pprint import pprint

data = json.load(open('ratrings.json'))

for something in data["users"]:
	pprint(something["name"])