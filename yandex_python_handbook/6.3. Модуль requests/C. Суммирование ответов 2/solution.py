from requests import get

address = 'http://' + input()
data = get(address).json()
print(sum(i for i in data if type(i) is int))