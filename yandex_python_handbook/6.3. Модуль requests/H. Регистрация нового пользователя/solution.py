from requests import post

address = 'http://' + input() + '/users'
data = {}
data["username"] = input()
data["last_name"] = input()
data["first_name"] = input()
data["email"] = input()
post(address, json=data)