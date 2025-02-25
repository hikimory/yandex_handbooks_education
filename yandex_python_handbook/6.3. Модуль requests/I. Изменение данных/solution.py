from requests import put
from sys import stdin

address = 'http://' + input() + '/users/' + input()
lines = [i.strip().split('=') for i in stdin]
data = {}
for libe in lines:
    data[libe[0]] = libe[1]
put(address, json=data)