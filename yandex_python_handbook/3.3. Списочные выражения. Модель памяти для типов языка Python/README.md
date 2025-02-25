# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 3.3

### 3.3. Списочные выражения. Модель памяти для типов языка Python

A. Список квадратов
```python
[x**2 for x in range(a, b + 1)]
```

B. Таблица умножения 2.0
```python
[[j for j in range(i, i*n + 1, i)] for i in range(1, n + 1)]
[[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
```

C. Длины всех слов
```python
[len(s) for s in sentence.split()]
```

D. Множество нечетных чисел
```python
{x for x in numbers if x % 2 != 0}
```

E. Множество всех полных квадратов
```python
{x for x in numbers if (x ** 0.5).is_integer()}
```

F. Буквенная статистика
```python
{char: text.lower().count(char) for char in set(text.lower()) if char.isalpha()}
```

G. Делители
```python
{number: [i for i in range(1, number + 1) if number % i == 0] for number in numbers}
```

H. Аббревиатура
```python
''.join([word[0].upper() for word in string.split()])
```

I. Преобразование в строку
```python
' - '.join([str(num) for num in sorted(set(numbers))])
```

J. RLE наоборот
```python
''.join([ch * count for ch, count in rle])
```