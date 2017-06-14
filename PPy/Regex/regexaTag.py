import re, urllib


# <a href="/advanced_search?hl=en-IN&amp;authuser=0">Advanced search</a>
websites = ['google']
# pattern = re.compile(r'<a.*>.*</a>+', re.I | re.M)
pattern = re.compile(r'href.*')
for website in websites:
	print("Searching for website: {}".format(website))
	try:
		response = urllib.urlopen("https://www." + website + ".com")
	except:
		print("Failed to open website https://www." + website + ".com")
	
	text = response.read()
	# print(text)
	title = re.findall(pattern, str(text))
	for t in title:
		t = t.split("href")
		print("Print {}".format(t))
