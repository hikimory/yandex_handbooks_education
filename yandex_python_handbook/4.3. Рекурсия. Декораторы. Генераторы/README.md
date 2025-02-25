# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 4.3

### 4.3. Рекурсия. Декораторы. Генераторы

A. Рекурсивный сумматор
```python
def recursive_sum(*args):
    if not args:
        return 0
    return args[-1] + recursive_sum(*args[:-1])
```

B. Рекурсивный сумматор цифр
```python
def recursive_digit_sum(number):
    if number == 0:
        return 0
    return number % 10 + recursive_digit_sum(number // 10)
```

C. Многочлен N-ой степени
```python
def make_equation(*coefs):
    if len(coefs) == 1:
        return coefs[0]
    return f"({make_equation(*coefs[:-1])}) * x + {coefs[-1]}"
```

D. Декор результата
```python
def answer(old_func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {old_func(*args, **kwargs)}"
    
    return new_func
```

E. Накопление результата
```python
def result_accumulator(old_func):
    queue = []

    def new_func(*args, method="accumulate"):
        nonlocal queue
        queue.append(old_func(*args))
        if method == "drop":
            result = queue.copy()
            queue.clear()
            return result

    return new_func
```

F. Сортировка слиянием
```python
def merge(left, right):
    merged_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    while i < len(left):
        merged_list.append(left[i])
        i += 1

    while j < len(right):
        merged_list.append(right[j])
        j += 1

    return merged_list


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)
```

G. Однотипность не порок
```python
def same_type(old_func):
    def new_func(*args):
        if len({type(x) for x in args}) > 1:
            print("Обнаружены различные типы данных")
            return False
        return old_func(*args)
    
    return new_func
```

H. Генератор Фибоначчи
```python
def fibonacci(n):
    prev, curr = 0, 1
    for i in range(n):
        yield prev
        prev, curr = curr, prev + curr
```

I. Циклический генератор
```python
def cycle(items):
    while True:
        for item in items:
            yield item
```

J. «Выпрямление» списка
```python
def make_linear(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(make_linear(item))
        else:
            result.append(item)
    return result
```