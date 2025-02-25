# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 4.2

### 4.2. Позиционные и именованные аргументы. Функции высших порядков. Лямбда-функции

A. Генератор списков
```python
def make_list(length, value=0):
    return [value for _ in range(length)]
```

B. Генератор матриц
```python
def make_matrix(size, value=0):
    if isinstance(size, tuple):
        width, height = size
    else:
        width, height = size, size
    return [[value for _ in range(width)] for _ in range(height)]
```

C. Функциональный НОД 2.0
```python
def gcd(*numbers):
    a = 0
    for b in numbers:
        while b:
            a, b = b, a % b
    return a
```

D. Имя of the month 2.0
```python
def month(number, lang="ru"):
    monthes = {
        "ru": ["Январь", "Февраль", "Март", "Апрель", 
               "Май", "Июнь", "Июль", "Август", 
               "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        "en": ["January", "February", "March", "April", 
               "May", "June", "July", "August", 
               "September", "October", "November", "December"]
    }
    return monthes[lang][number - 1]
```

E. Подготовка данных
```python
def to_string(*elements, sep=" ", end="\n"):
    return sep.join(map(str, elements)) + end
```

F. Кофейня
```python
def order(*preferences):
    recipes = {
        "Эспрессо": {"coffee": 1},
        "Капучино": {"coffee": 1, "milk": 3},
        "Макиато": {"coffee": 2, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2},
        "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
        "Кон Панна": {"coffee": 1, "cream": 1}
    }
    for drink in preferences:
        ingredients = recipes[drink]
        find_in_stock = dict(filter(lambda x: in_stock[x[0]] >= x[1], ingredients.items()))
        if len(ingredients) == len(find_in_stock):
            for i in ingredients:
                in_stock[i] -= ingredients[i]
            return drink
    return "К сожалению, не можем предложить Вам напиток"
```

G. В эфире рубрика «Эксперименты»
```python
def enter_results(*numbers):
    results.extend(numbers)


def get_sum():
    total_sum = round(sum(results[::2]), 2), round(sum(results[1::2]), 2)
    return tuple(total_sum)


def get_average():
    average = map(lambda x: round(x * 2 / len(results), 2), get_sum())
    return tuple(average)


results = []
```

H. Длинная сортировка
```python
lambda x: (len(x), x.lower())
```

I. Чётная фильтрация
```python
lambda x: sum(map(int, str(x))) % 2 == 0
```

J. Ключевой секрет
```python
def secret_replace(text, **kwargs):
    result = ''
    newargs = {d: (v, 0) for d, v in kwargs.items()}
    for i in text:
        if i in newargs:
            result += newargs[i][0][newargs[i][1] % len(newargs[i][0])]
            newargs[i] = newargs[i][0], newargs[i][1] + 1
        else:
            result += i
    return result
```