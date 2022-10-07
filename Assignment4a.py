import requests
import json

# username = input("please input username of github:")
username = lovelifecat

url = 'https://api.github.com/users/%s/repos' % username

r = requests.get(url)
for i in range(len(r.json())):
    Name = r.json()[i]['name']
    UrlOfCommit = 'https://api.github.com/repos/%s/%s/commits' % (username, Name)
    c = requests.get(UrlOfCommit)
    Number = len(c.json())
    print(Name + " Number of commit: " + str(Number))
