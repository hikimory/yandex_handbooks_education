from requests import get
from sys import stdin

address = 'http://' + input()
paths = [i.strip() for i in stdin]
total_summ = 0
for path in paths:
    total_summ += sum(get(address + path).json())
print(total_summ)