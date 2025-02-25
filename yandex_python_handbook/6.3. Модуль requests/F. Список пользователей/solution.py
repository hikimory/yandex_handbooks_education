from requests import get

address = 'http://' + input() + '/users'
data = get(address).json()
names = []
for i in data:
    names.append(f"{i['last_name']} {i['first_name']}")
sorted_names = sorted(names)
for name in sorted_names:
    print(name)