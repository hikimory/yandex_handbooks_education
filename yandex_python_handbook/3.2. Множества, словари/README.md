# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 3.2

### 3.2. Множества, словари

A. Символическая выжимка
```python
print(*set(input()), sep='')
print(''.join(set(input())))   
```
B. Символическая разница
```python
print(*(set(input()) & set(input())), sep='')
print(*(set(input())intersection(set(input()))), sep='')
print(''.join(set(input()).intersection(set(input()))))
```
C. Зайка — 8
```python
objects = []
for _ in range(int(input())):
    objects.extend(input().split())
print('\n'.join(set(objects)))
```
D. Кашееды
```python
a, b = int(input()), int(input())
semolina, oatmeal = set(), set()
for _ in range(a):
    semolina.add(input())
for _ in range(b):
    oatmeal.add(input())
both = len(semolina & oatmeal) # both = len(semolina.intersection(oatmeal))
print(both if both else 'Таких нет')
```
E. Кашееды — 2
```python
n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    children.add(input())
count = len(children) * 2 - (n + m)
print(count if count else 'Таких нет')
```
F. Кашееды — 3
```python
n, m = int(input()), int(input())
children = set()
for _ in range(n + m):
    child = input()
    if child in children:
        children.remove(child)
    else:
        children.add(child)
print("\n".join(sorted(children)) if len(children) else 'Таких нет')
```
G. Азбука Морзе
```python
MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----."
}

for word in input().upper().split():
    encoded_word = []
    for char in word:
        encoded_word.append(MORSE[char])
    print(" ".join(encoded_word))
```
H. Кашееды — 4
```python
a, kids = int(input()), []
for _ in range(a):
    kids.extend([input().split()])
kids.sort()
key, counter = input(), 0
for kid in kids:
    if key in kid[1:]:
        print(kid[0])
        counter += 1
if not counter:
    print('Таких нет')
```
I. Зайка — 9
```python
animals = dict()
while (line := input()) != "":
    for item in line.split():
        animals[item] = animals.get(item, 0) + 1
for animal, count in animals.items():
    print(animal, count)
```
J. Транслитерация
```python
RULES = {
    "А": "A", "Б": "B", "В": "V", "Г": "G",
    "Д": "D", "Е": "E", "Ё": "E", "Ж": "Zh",
    "З": "Z", "И": "I", "Й": "I", "К": "K",
    "Л": "L", "М": "M", "Н": "N", "О": "O",
    "П": "P", "Р": "R", "С": "S", "Т": "T",
    "У": "U", "Ф": "F", "Х": "Kh", "Ц": "Tc",
    "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ъ": "",
    "Ы": "Y", "Ь": "", "Э": "E", "Ю": "Iu", 
    "Я": "Ia"
}
result = ""
for char in input():
    new_char = RULES.get(char.upper(), char)
    if char.islower():
        new_char = new_char.lower()
    result += new_char
print(result)
```
K. Однофамильцы
```python
persons = set()
uniques = set()
for _ in range(count := int(input())):
    name = input()
    if name in persons:
        uniques.discard(name)
    else:
        persons.add(name)
        uniques.add(name)
print(count - len(uniques))
```
L. Однофамильцы — 2
```python
people = []
for _ in range(int(input())):
    people.append(input())
people = [i + ' - ' + str(people.count(i)) for i in set(people) if people.count(i) > 1]
if people:
    for x in sorted(people):
        print(x)
else:
    print('Однофамильцев нет')
```
M. Дайте чего-нибудь новенького!
```python
menu, new_menu = set(), set()
for _ in range(int(input())):
    menu.add(input())
for _ in range(int(input())):
    for j in range(int(input())):
        new_menu.add(input())
diff = sorted(menu - new_menu)  # menu.difference(new_menu)
if diff:
    print(*diff, sep='\n')
else:
    print('Готовить нечего')
```
N. Это будет шедевр!
```python
ingredients, dishes = set(), []

for _ in range(int(input())):
    ingredients.add(input())

for _ in range(int(input())):
    dish = input()
    dish_ingredients = set()
    for i in range(int(input())):
        dish_ingredients.add(input())
    if ingredients >= dish_ingredients:
        dishes.append(dish)

if dishes:
    print(*sorted(dishes), sep="\n")
else:
    print('Готовить нечего')
```
O. Двоичная статистика!
```python
data = []
for i in list(map(lambda x: bin(int(x))[2:], input().split())):
    data.append({"digits": len(i),
                 "units": i.count('1'),
                 "zeros": i.count('0')})
print(data)
```
P. Зайка — 10
```python
result = set()
while (line := input()) != "":
    items = line.split()
    for i in range(len(items)):
        if items[i] == "зайка":
            if i > 0:
                result.add(items[i - 1])
            if i < len(items) - 1:
                result.add(items[i + 1])
print(*result, sep='\n')
```
Q. Друзья друзей
```python
#  не допер решение
```
R. Карта сокровищ
```python
counters = dict()
for _ in range(int(input())):
    x, y = input().split()
    group = x[:-1] + " " + y[:-1]
    counters[group] = counters.get(group, 0) + 1
print(max(counters.values()))
```
S. Частная собственность
```python
data = []
for _ in range(int(input())):
    k = set(input().split(": ")[1].split(", "))
    data.extend(k)
data = sorted(toy for toy in data if data.count(toy) == 1)
print(*data, sep='\n')
```
T. Простая задача 4.0
```python
numbers = []
for n in set(input().split("; ")):
    numbers.append(int(n))
numbers.sort()
primes = dict()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        while b:
            a, b = b, a % b
        if a == 1:
            primes[numbers[i]] = primes.get(numbers[i], []) + [str(numbers[j])]
            primes[numbers[j]] = primes.get(numbers[j], []) + [str(numbers[i])]
    if numbers[i] in primes:
        print(f"{numbers[i]} - {', '.join(primes[numbers[i]])}")
```