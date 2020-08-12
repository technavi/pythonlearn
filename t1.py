import requests
response=requests.get('https://randomuser.me/api?results=10')
data=response.json()
for item in data['results']:
    print(item['name']['first'])
    print(item['location']['country'])