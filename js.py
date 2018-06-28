import requests
token='18b2b30b3892c067c678ac06f4e9273e9bf89b73'
headers = {'Authorization': 'token ' + token}

login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())
print login.status_code
""" r=requests.get('https://api.github.com/events')
print r.json()
print r.status_code """
