import requests

def GetRepoNameAndCommit(username):
    url = 'https://api.github.com/users/%s/repos' % username
    r = requests.get(url)
    for i in range(len(r.json())):
        if len(r.json()) == 0:
            return False
        else:
            Name = r.json()[i]['name']
            UrlOfCommit = 'https://api.github.com/repos/%s/%s/commits' % (username, Name)
            c = requests.get(UrlOfCommit)
            Number = len(c.json())
            print(Name + " Number of commit: " + str(Number))
            return True
    

if __name__ == '__main__':
    username = input("please input your username: ")
    GetRepoNameAndCommit(username)
