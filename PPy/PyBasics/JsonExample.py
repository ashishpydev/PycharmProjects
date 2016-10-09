import json

book = {}

book['Tom'] = {
	'name': 'Tom',
	'Address': 'BTM, Bangalore, IND',
	'Phone': 45464567
}
book['Bob'] = {
	'name': 'Bob',
	'Address': 'HSR, Bangalore, IND',
	'Phone': 43565464
}

s = json.dumps(book)

with open("/Users/ashishagrawal/PycharmProjects/learnPython/book", 'w') as f:
	f.write(s)
	f.close()

with open ("/Users/ashishagrawal/PycharmProjects/learnPython/book", 'r') as f:
	s = f.read()
	s = json.loads(s)
	print(s)
	print(s['Bob']['Address'])
	f.close()
