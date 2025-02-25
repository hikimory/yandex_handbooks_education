# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 3.5

### 3.5. Потоковый ввод/вывод. Работа с текстовыми файлами. JSON

A. A+B+...
```python
from sys import stdin

total_sum = 0
for line in stdin:
    for n in line.split():
        total_sum += int(n)
print(total_sum)
```

B. Средний рост
```python
from sys import stdin

count, difference = 0, 0
for line in stdin:
    info = line.split()
    difference += int(info[2]) - int(info[1])
    count += 1
print(round(difference / count))
```

C. Без комментариев 2.0
```python
from sys import stdin

res = [x[:x.find("#")] for x in stdin.readlines() if not x.startswith("#")]
print(*res, sep='\n')
```

D. Найдётся всё 2.0
```python
from sys import stdin

lines = stdin.readlines()
query = lines.pop().rstrip("\n").lower()
res = [x.rstrip("\n") for x in lines if query in x.lower()]
print(*res, sep='\n')
```

E. А роза упала на лапу Азора 6.0
```python
from sys import stdin

result = set()
for word in stdin.read().split():
    n = len(word)
    if word[:n // 2].lower() == word[:(n - 1) // 2:-1].lower():
        result.add(word)
print("\n".join(sorted(result)))
```

F. Транслитерация 2.0
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

with open("cyrillic.txt", "r", encoding="UTF-8") as file_in:
    text = file_in.read()

translit = ""
for char in text:
    new_char = RULES.get(char.upper(), char)
    if char.islower():
        new_char = new_char.lower()
    translit += new_char

with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(translit)
```

G. Файловая статистика
```python
with open(input(), "r", encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]
print(count := len(numbers))
print(len([x for x in numbers if x > 0]))
print(min(numbers))
print(max(numbers))
print(total_sum := sum(numbers))
print(round(total_sum / count, 2))
```

H. Файловая разница
```python
words = []
for _ in range(2):
    with open(input(), "r", encoding="UTF-8") as file_in:
        words.append(set(file_in.read().split()))

with open(input(), "w", encoding="UTF-8") as file_out:
    print(*sorted(words[0] ^ words[1]), sep='\n', file=file_out) # words[0].symmetric_difference(words[1])
```

I. Файловая чистка
```python
import re

lines = []
with open(input(), "r", encoding="UTF-8") as file_in:
    for line in file_in:
        
        line = line.replace('\t', '')
        line = re.sub(r' +', ' ', line)
        line = re.sub(r'\n+', '', line)
        line = line.strip().rstrip()

        if line != "":
            lines.append(line + "\n")

with open(input(), "w", encoding="UTF-8") as file_out:
    file_out.writelines(lines)
```

J. Хвост
```python
file_in_name, tail = input(), int(input())

with open(file_in_name, 'r', encoding="UTF-8") as f:
    lines = f.readlines()
    
    if tail > len(lines):
        tail = len(lines)

    for line in lines[-tail:]:
        print(line.rstrip('\n'))
```

K. Файловая статистика 2.0
```python
import json

with open(input(), "r", encoding="UTF-8") as file_in:
    numbers = [int(x) for x in file_in.read().split()]

statistics = {
    "count": (count := len(numbers)),
    "positive_count": len([x for x in numbers if x > 0]),
    "min": min(numbers),
    "max": max(numbers),
    "sum": (total_sum := sum(numbers)),
    "average": round(total_sum / count, 2)
}

with open(input(), "w", encoding="UTF-8") as file_out:
    json.dump(statistics, file_out, ensure_ascii=False, indent=4)
```

L. Разделяй и властвуй
```python
groups = ([], [], [])
with open(input(), "r", encoding="UTF-8") as file_in:
    for line in file_in:
        line_groups = ([], [], [])
        for number in line.split():
            even = sum(1 for x in number if int(x) % 2 == 0)
            if even * 2 > (length := len(number)):
                ind = 0
            elif even * 2 < length:
                ind = 1
            else:
                ind = 2
            line_groups[ind].append(number)
        for ind in range(3):
            groups[ind].append(" ".join(line_groups[ind]) + "\n")

for group in groups:
    with open(input(), "w", encoding="UTF-8") as file_out:
        file_out.writelines(group)
```

M. Обновление данных
```python
import json
from sys import stdin

with open(file_name := input(), "r", encoding="UTF-8") as file_in:
    content = json.load(file_in)

for line in stdin:
    variable, value = line.rstrip("\n").split(" == ")
    content[variable] = value

with open(file_name, "w", encoding="UTF-8") as file_out:
    json.dump(content, file_out, ensure_ascii=False, indent=4)
```

N. Слияние данных
```python
import json

with open(users_file_name := input(), "r", encoding="UTF-8") as file_in:
    users = json.load(file_in)

with open(input(), "r", encoding="UTF-8") as file_in:
    updates = json.load(file_in)

result = dict()
for user in users:
    result[user["name"]] = {key: value for key, value in user.items() if key != "name"}
for user in updates:
    for key, value in user.items():
        if key != "name" and value > result[user["name"]].get(key, ""):
            result[user["name"]][key] = value

with open(users_file_name, "w", encoding="UTF-8") as file_out:
    json.dump(result, file_out, ensure_ascii=False, indent=4)
```

O. Поставь себя на моё место
```python
import json

with open("scoring.json", "r", encoding="UTF-8") as file_in:
    scoring = json.load(file_in)

points = 0
for group in scoring:
    counter = sum(1 for test in group["tests"] if test["pattern"] == input())
    points += counter * group["points"] // len(group["tests"])
print(points)
```

P. Найдётся всё 3.0
```python
from sys import stdin

query = input().lower()
flag = False
for file_name in stdin.read().split():
    with open(file_name, "r", encoding="UTF-8") as file_in:
        if query in " ".join(file_in.read().replace("&nbsp;", " ").lower().split()):
            print(file_name)
            flag = True
if not flag:
    print("404. Not Found")
```

Q. Прятки
* % n ограничивает результат диапазоном [0, n-1].
* & mask выделяет определенные биты, в соответствии с битами, установленными в mask.

```python
# version 1
with open("secret.txt", "r", encoding="UTF-8") as file_in:
    print("".join(chr(ord(x) % 256) for x in file_in.read()))

# version 2
with open("secret.txt", "r", encoding="UTF-8") as file_in:
    hidden_message = ""
    for char in file_in.read():
        code = ord(char)
        extracted_code = code & 0x7F  # Выделяем младший байт (младшие 7 бит)
        if extracted_code < 128:
            hidden_message += chr(extracted_code)
    print(hidden_message)
```

R. Сколько вешать в байтах?
```python
import os
import math

UNITS = ["Б", "КБ", "МБ", "ГБ"]
size, ind = os.path.getsize(input()), 0
while size >= 1024 and ind < len(UNITS) - 1:
    size = math.ceil(size / 1024)
    ind += 1
print(f"{size}{UNITS[ind]}")
```

S. Это будет наш секрет
```python
# version 1
shift = int(input())

with open("public.txt", "r", encoding="UTF-8") as file_in:
    public = file_in.read()

result = list(public.lower())
for i in range(len(result)):
    if result[i].isalpha():
        result[i] = chr('a' + (ord(result[i]) - ord('a') + shift) % 26)
    if public[i].isupper():
        result[i] = result[i].upper()

with open("private.txt", "w") as file_out:
    print(''.join(result), file=file_out)

# version 2
LETTERS = "abcdefghijklmnopqrstuvwxyz"
shift = int(input())

with open("public.txt", "r", encoding="UTF-8") as file_in:
    public = file_in.read()

private = list(public.lower())
for i in range(len(private)):
    if private[i] in LETTERS:
        private[i] = LETTERS[(LETTERS.index(private[i]) + shift) % len(LETTERS)]
    if public[i].isupper():
        private[i] = private[i].upper()

with open("private.txt", "w", encoding="UTF-8") as file_in:
    file_in.write("".join(private))
```

T. Файловая сумма
Представьте себе, что у нас есть два байта:

byte1 (старший байт)

byte2 (младший байт)

Каждый из этих байтов может принимать значения от 0 до 255. Мы хотим объединить их в одно 2-байтовое число. Когда мы "склеиваем" два байта вместе, мы как бы "сдвигаем" старший байт на 8 битов влево, чтобы освободить место для младшего байта.

Число 256 получается из-за того, что у нас 8 бит в байте. 2 в степени 8 как раз равно 256. То есть, умножая старший байт на 256, мы "сдвигаем" его значение на 8 битов влево, что эквивалентно умножению на 256 в десятичной системе счисления.

Пример:
Пусть byte1 = 2, а byte2 = 10. Тогда:

byte1 (в двоичном виде): 00000010

byte2 (в двоичном виде): 00001010

Сдвигаем byte1 на 8 битов влево: 00000010 00000000 (это эквивалентно умножению byte1 на 256). Добавляем byte2 к результату: 00000010 00001010

В результате получается 2-байтовое число 00000010 00001010. Если мы переведем это число в десятичную систему счисления, то получим 522.

Один байт состоит из 8 бит.
Два байта составляют 16 бит (8 бит + 8 бит).
Максимальное число, которое можно представить с помощью 16 бит, равно 2<sup>16</sup> - 1 = 65535.
Когда мы суммируем несколько 2-байтовых чисел, результат может превысить 65535.  В этом случае нам нужно "обрезать" результат, чтобы он снова попал в диапазон 0-65535.
```python
# version 1
with open("numbers.num", "rb") as file_in:
    data = file_in.read()
print(sum(data[i] * 256 + data[i + 1] for i in range(0, len(data), 2)) % 65536)

# version 2
total_sum = 0
with open("numbers.num", "rb") as f:
    while True:
        byte1 = f.read(1)
        byte2 = f.read(1)
        if not byte1 or not byte2:
            break  # Достигнут конец файла
        total_sum += (ord(byte1) << 8) + ord(byte2)  # Сдвигаем байты и складываем
print(total_sum % 65536)
```