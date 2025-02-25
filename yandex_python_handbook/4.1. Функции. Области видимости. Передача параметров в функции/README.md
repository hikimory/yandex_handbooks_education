# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 4.1

### 4.1. Функции. Области видимости. Передача параметров в функции

A. Функциональное приветствие
```python
def print_hello(name):
    print(f"Hello, {name}!")
```

B. Функциональный НОД
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

C. Длина числа
```python
# v1
def number_length(a):
    return len(str(a).lstrip("-"))

# v2
def number_length(number):
    return len(str(abs(number)))
```

D. Имя of the month
```python
def month(n, lang):
    monthes = {
        "ru": ["Январь", "Февраль", "Март", "Апрель", 
               "Май", "Июнь", "Июль", "Август", 
               "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        "en": ["January", "February", "March", "April", 
               "May", "June", "July", "August", 
               "September", "October", "November", "December"]
    }
    return monthes[lang][n - 1]
```

E. Числовая строка
```python
def split_numbers(numbers):
    return tuple(int(x) for x in numbers.split())
```

F. Модернизация системы вывода
```python
def modern_print(phrase):
    if phrase not in used_phrases:
        used_phrases.add(phrase)
        print(phrase)


used_phrases = set()
```

G. Шахматный «обед»
```python
def can_eat(knight_position, piece_position):
    knight_row, knight_col = knight_position
    piece_row, piece_col = piece_position

    row_diff = abs(knight_row - piece_row)
    col_diff = abs(knight_col - piece_col)

    return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
```

H. А роза упала на лапу Азора 7.0
```python
def is_palindrome(x):
    if isinstance(x, int):
        x = str(x)
    n = len(x)
    if x[0:n // 2] == x[-1:-1 - n // 2:-1]:
        return True
    return False
```

I. Простая задача 5.0
```python
def is_prime(n):
    if n == 1 or (n > 2 and n % 2 == 0):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```

J. Слияние
```python
def merge(tuple1, tuple2):
    merged_list = []
    i = 0
    j = 0

    while i < len(tuple1) and j < len(tuple2):
        if tuple1[i] <= tuple2[j]:
            merged_list.append(tuple1[i])
            i += 1
        else:
            merged_list.append(tuple2[j])
            j += 1

    while i < len(tuple1):
        merged_list.append(tuple1[i])
        i += 1

    while j < len(tuple2):
        merged_list.append(tuple2[j])
        j += 1

    return tuple(merged_list)
```