from requests import get

address = 'http://' + input()
summ = 0
while True:
    data = int(get(address).text)
    if not data:
        break
    summ += data
print(summ)