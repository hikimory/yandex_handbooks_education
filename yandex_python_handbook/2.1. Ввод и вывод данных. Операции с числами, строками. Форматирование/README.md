# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 2.1

### 2.1. Ввод и вывод данных. Операции с числами, строками. Форматирование

A. Привет, Яндекс!
```python
print("Привет, Яндекс!")
```

B. Привет, всем!
```python
print("Как Вас зовут?")
name = input()
print(f"Привет, {name}")
```

C. Излишняя автоматизация
```python
phrase = input()
print(f"{phrase}\n" * 3, end='')
```

D. Сдача
```python
money = int(input())
print(int(money - 2.5 * 38))
```

E. Магазин
```python
price = int(input())
weight = int(input())
money = int(input())
print(money - weight * price)
```

F. Чек
```python
item = input()
price = int(input())
weight = int(input())
money = int(input())
print("Чек")
print(f"{item} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - price * weight}руб")
```

G. Делу — время, потехе — час
```python
count = int(input())
phrase = "Купи слона!"
print((phrase + "\n") * count, sep='')
```

H. Наказание
```python
count = int(input())
phrase = input()
print(f'Я больше никогда не буду писать "{phrase}"!\n' * count, end='')
```

I. Деловая колбаса
```python
minutes = int(input())
children = int(input())
print(children * minutes // 2)
```

J. Детский сад — штаны на лямках
```python
name = input()
number = input()
print(f'Группа №{number[0]}.')
print(f'{number[2]}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number[1]}.')
```

K. Автоматизация игры
```python
n = int(input())
print(n // 100 % 10, n // 1000, n % 10, n // 10 % 10, sep="")

n = input()
print(f'{n[1]}{n[0]}{n[3]}{n[2]}')
```

L. Интересное сложение
```python
a = int(input())
b = int(input())
result = (a % 10 + b % 10) % 10 \
         + (a // 10 % 10 + b // 10 % 10) % 10 * 10 \
         + (a // 100 % 10 + b // 100 % 10) % 10 * 100
print(result)
```

M. Дед Мороз и кофеты
```python
children = int(input())
candies = int(input())
print(candies // children)
print(candies % children)
```

N. Шарики и ручки
```python
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)
```

O. В ожидании доставки
```python
hours = int(input())
minutes = int(input())
duration = int(input())
time_sum = (minutes + duration)
delivery_minutes = time_sum % 60
delivery_hours = (hours + time_sum // 60) % 24
print(f"{str(delivery_hours):0>2}:{str(delivery_minutes):0>2}")
```

P. Доставка
```python
warehouse = int(input())
store = int(input())
speed = int(input())
print(f"{(store - warehouse) / speed:.2f}")
```

Q. Ошибка кассового аппарата
```python
total = int(input())
last_order = int(input(), 2)
print(total + last_order)
```

R. Сдача 10
```python
price = int(input(), 2)
money = int(input())
print(money - price)
```

S. Украшение чека
```python
product = input()
price = int(input())
weight = int(input())
money = int(input())
print(f"{'Чек':=^35}")
print("Товар:", f"{product: >28}")
print("Цена:", f"{f'{weight}кг * {price}руб/кг': >29}")
print("Итого:", f"{weight * price: >25}руб")
print("Внесено:", f"{money: >23}руб")
print("Сдача:", f"{money - weight * price: >25}руб")
print("=" * 35)
```

T. Мухи отдельно, котлеты отдельно
```python
weight = int(input())
price = int(input())
first_price = int(input())
second_price = int(input())
first_weight = (price - second_price) * weight // (first_price - second_price)
second_weight = weight - first_weight
print(first_weight, second_weight)
```