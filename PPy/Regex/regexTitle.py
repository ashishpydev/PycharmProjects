import re, urllib

try:
	import urllib.request
except:
	pass

websites = ['google', 'yahoo', 'youtube']
pattern = re.compile(r'<a>\s?[a-z]{1-4}</a>', re.I|re.M)

for website in websites:
	print("Searching for website: {}".format(website))
	try:
		response = urllib.urlopen("https://www." + website + ".com")
	except:
		print("Failed to open website https://www." + website + ".com")
	
	text = response.read()
	print(text)
	title = re.findall(pattern, str(text))
	print(title)
