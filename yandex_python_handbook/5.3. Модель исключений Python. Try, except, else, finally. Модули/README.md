# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 5.3

### 5.3. Модель исключений Python. Try, except, else, finally. Модули

A. Обработка ошибок
```python
try:
    func()
except Exception as e:
    print(e.__class__.__name__) # type(error).__name__
else:
    print("No Exceptions")
```

B. Ломать — не строить
```python
try:
    func(None, None)
except Exception:
    print("Ура! Ошибка!")
```

C. Ломать — не строить 2
```python
class Test:
    def __repr__(self):
        raise Exception

    def __str__(self):
        raise Exception


try:
    func(Test())
except Exception:
    print("Ура! Ошибка!")
```

D. Контроль параметров
```python
def only_positive_even_sum(a, b):
    if not all(isinstance(x, int) for x in (a, b)):
        raise TypeError
    if not all(x > 0 and x % 2 == 0 for x in (a, b)):
        raise ValueError
    return a + b
```

E. Слияние с проверкой
```python
def check_iterability(x):
    try:
        iter(x)
    except Exception:
        raise StopIteration


def check_type(elements):
    el_type = type(elements[0])
    for i in range(len(elements) - 1):
        if not isinstance(elements[i], el_type):
            raise TypeError


def check_sorting(elements):
    for i in range(len(elements) - 1):
        if elements[i] > elements[i + 1]:
            raise ValueError


def merge(left, right):
    check_iterability(left)
    check_iterability(right)
    check_type((*left, *right))
    check_sorting(left)
    check_sorting(right)

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
```

F. Корень зла 2
1. Все коэффициенты равны нулю $(a = 0, b = 0, c = 0)$:

    Уравнение: $0x^2 + 0x + 0 = 0$
    Что происходит: В этом случае, уравнение превращается в $0 = 0$. Это верно для любого значения $x$.
    Решение: Любое число является решением. Уравнение имеет бесконечно много решений. Это тривиальный, но важный случай, который нужно обрабатывать, чтобы избежать некорректной работы программы.

2. Коэффициенты a и b равны нулю $(a = 0, b = 0, c ≠ 0)$:

    Уравнение: $0x^2 + 0x + c = 0$
    Что происходит: Уравнение превращается в $c = 0$. Поскольку c не равно нулю по условию, то уравнение не имеет решений.
    Решение: Нет решений.

3. Только коэффициент a равен нулю $(a = 0, b ≠ 0, c ≠ 0)$:

    Уравнение: $0*x^2 + bx + c = 0$, что упрощается до $bx + c = 0$
    Что происходит: Это линейное уравнение.
    Решение: $x = -c / b$

4. Коэффициент a не равен нулю $(a ≠ 0)$:

    Уравнение: $ax^2 + bx + c = 0$
    Что происходит: Это полноценное квадратное уравнение.
    Решение: Решается через дискриминант (D):
    
    $D = b^2 - 4ac$

    Если $D > 0$: два различных вещественных корня:

    $x1 = (-b + sqrt(D)) / (2a)$

    $x2 = (-b - sqrt(D)) / (2a)$

    Если D = 0: один вещественный корень (или два совпадающих):

    $x = -b / (2a)$

    Если $D < 0$: два комплексных корня (нет решения):

    $x1 = (-b + i*sqrt(-D)) / (2a)$

    $x2 = (-b - i*sqrt(-D)) / (2a)$

```python
class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        raise TypeError
    d = b ** 2 - 4 * a * c
    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError
    elif (a == 0 and b == 0) or d < 0:
        raise NoSolutionsError
    elif a == 0:
        roots = [-c / b, -c / b]
    elif d == 0:
        roots = [-b / (2 * a), -b / (2 * a)]
    else:
        roots = [(-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)]
    return tuple(roots)
```

G. Валидация имени
```python
class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name
```

H. Валидация имени пользователя
```python
class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username
```

I. Валидация пользователя
```python
class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(**kwargs):
    if set(kwargs) != {"last_name", "first_name", "username"}:
        raise KeyError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
```

J. Валидация пароля
```python
from hashlib import sha256


class MinLengthError(ValueError):
    pass


class PossibleCharError(ValueError):
    pass


class NeedCharError(ValueError):
    pass


def password_validation(password, min_length=8, 
                        possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    elif len(password) < min_length:
        raise MinLengthError
    elif not all(x in possible_chars for x in password):
        raise PossibleCharError
    elif not any(at_least_one(x) for x in password):
        raise NeedCharError
    return sha256(password.encode("utf-8")).hexdigest()
```