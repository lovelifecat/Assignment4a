import requests

def GetRepoNameAndCommit(username):
    url = 'https://api.github.com/users/%s/repos' % username
    r = requests.get(url)
    print(r.status_code)

    if r.status_code != 200:
        return False
    else:
        for i in range(len(r.json())):
            Name = r.json()[i]['name']
            UrlOfCommit = 'https://api.github.com/repos/%s/%s/commits' % (username, Name)
            c = requests.get(UrlOfCommit)
            Number = len(c.json())
            print(Name + " Number of commit: " + str(Number))
        return True


if __name__ == '__main__':
    username = input("please input your username: ")
    GetRepoNameAndCommit(username)
