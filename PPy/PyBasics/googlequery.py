import urllib
import json

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
# query = input()
# print(query)
query = urllib.urlencode({'q': "Start"})

response = urllib.urlopen(url + query).read()

data = json.loads(response)

results = data['responseData']['results']

for result in results:
    title = result['title']
    url = result['url']
    print (title + '; ' + url)
