# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 2.3

### 2.3. Циклы

A. Раз, два, три! Ёлочка, гори!
```python
while input() != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")
```

B. Зайка — 3
```python
counter = 0
while (line := input()) != "Приехали!":
    if "зайка" in line:
        counter += 1
print(counter)
```

C. Считалочка
```python
start, finish = int(input()), int(input())
for i in range(start, finish + 1):
    print(i, end=" ")
```

D. Считалочка 2.0
```python
start, finish = int(input()), int(input())
step = 1
if start > finish:
    step = -1
for i in range(start, finish + step, step):
    print(i, end=" ")
```

E. Внимание! Акция!
```python
total_sum = 0
while (price := float(input())) != 0:
    if price < 500:
        total_sum += price
    else:
        total_sum += price * 0.9
print(total_sum)
```

F. НОД
```python
a = int(input())
b = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(a)
```

G. НОК
```python
a = c = int(input())
b = d = int(input())
while b:
    tmp = a
    a = b
    b = tmp % b
print(c * d // a)
```

H. Излишняя автоматизация 2.0
```python
phrase = input()
count = int(input())
for _ in range(count):
    print(phrase)
```

I. Факториал
```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```

J. Маршрут построен
```python
x = y = 0
while (direction := input()) != "СТОП":
    step = int(input())
    match direction:
        case "СЕВЕР":
            y += step
        case "ВОСТОК":
            x += step
        case "ЮГ":
            y -= step
        case "ЗАПАД":
            x -= step
print(y, x, sep="\n")
```

K. Цифровая сумма
```python
number = int(input())
digit_sum = 0
while number:
    digit_sum += number % 10
    number //= 10
print(digit_sum)
```

L. Сильная цифра
```python
number = int(input())
max_digit = 0
while number:
    max_digit = max(max_digit, number % 10)
    number //= 10
print(max_digit)
```

M. Первому игроку приготовиться 2.0
```python
count = int(input())
player = input()
for _ in range(count - 1):
    player = min(player, input())
print(player)
```

N. Простая задача
Простое число - натуральное число, большее 1, называется простым, если оно делится только на 1 и на само себя.
При определении простого числа достаточно проверять делимость только до квадратного корня из этого числа.

Доказательство
Предположим, что число n - составное (не простое). Это значит, что его можно разложить на два множителя:

$n = a * b$
Где $a$ и $b$ - целые числа, большие 1.

Допустим, что оба множителя $a$ и $b$ больше квадратного корня из n:

$a > √n$
$b > √n$

Тогда их произведение будет больше $n$:

$a * b > √n * √n$
$a * b > n$

Что противоречит нашему исходному уравнению $n = a * b.$
Следовательно, наше предположение о том, что оба множителя больше квадратного корня из $n$, неверно.
Это значит, что хотя бы один из множителей $a$ или $b$ должен быть меньше или равен квадратному корню из $n$.

Вывод
Eсли число N равно произведению двух других, то одно из них не больше корня из $N$, а другое не меньше корня из $N$.
Из этого следует, что если число N не делится ни на одно из чисел $2,3,4,…,$"корень из $N$", то оно не делится и ни на одно из чисел "корень из $N$"$+1,…,N−2,N−1$, так как если есть делитель больше корня (не равный N), то есть делитель и меньше корня (не равный 1). 
Поэтому в цикле for достаточно проверять числа не до $N$, а до корня.

Поэтому, чтобы проверить, является ли число n простым, достаточно проверить его делимость на все числа от 2 до квадратного корня из n включительно. Если ни одно из этих чисел не является делителем n, то число n - простое.

```python
n = int(input())

if n <= 1:
    print("NO")
elif n == 2:
    print("YES")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("YES")
    else:
        print("NO")

# 2 version
n = int(input())
is_prime = True
if n == 1 or (n > 2 and n % 2 == 0):
    is_prime = False
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("YES")
else:
    print("NO")
```

O. Зайка — 4
```python
counter = 0
for _ in range(int(input())):
    if "зайка" in input():
        counter += 1
print(counter)
```

P. А роза упала на лапу Азора 2.0
```python
number = int(input())
direct_number = str(number)
reversed_number = ""
while number:
    reversed_number += str(number % 10)
    number //= 10
if direct_number == reversed_number:
    print("YES")
else:
    print("NO")
```

Q. Чётная чистота
```python
number = int(input())
clean_number = ""
while number:
    if number % 10 % 2 != 0:
        clean_number = str(number % 10) + clean_number
    number //= 10
print(clean_number)
```

R. Простая задача 2.0
```python
number = int(input())
result = ""
for i in range(2, number):
    while number % i == 0:
        if len(result) > 0:
            result += " * " + str(i)
        else:
            result = str(i)
        number = number // i
print(result)
```

S. Игра в «Угадайку»
```python
left = 1
right = 1000
while left <= right:
    middle = (left + right) // 2
    print(middle)
    answer = input()
    if answer == "Меньше":
        right = middle - 1
    elif answer == "Больше":
        left = middle + 1
    else:
        break
```

T. Хайпанём немножечко!
```python
result = -1
h_prev = 0
for i in range(int(input())):
    b = int(input())
    m = b // 256 ** 2
    r = (b - m * 256 ** 2) // 256
    h = b - m * 256 ** 2 - r * 256
    if h >= 100 or h != 37 * (m + r + h_prev) % 256:
        result = i
        break
    h_prev = h
print(result)
```