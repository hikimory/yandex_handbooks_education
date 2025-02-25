# Ответы и решения задач из хэндбука Яндекс «Основы Python», параграф 2.2

### 2.2. Условный оператор

A. Просто здравствуй, просто как дела
```python
name = input("Как Вас зовут?\n")
print(f"Здравствуйте, {name}!")
answer = input("Как дела?\n")
if answer == "хорошо":
    print("Я за вас рада!")
else:
    print("Всё наладится!")
```

B. Кто быстрее?
```python
petya_speed = int(input())
vasya_speed = int(input())
if petya_speed > vasya_speed:
    print("Петя")
else:
    print("Вася")
```

C. Кто быстрее на этот раз?
```python
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())
max_speed = max(petya_speed, vasya_speed, tolya_speed)
if max_speed == petya_speed:
    print("Петя")
elif max_speed == vasya_speed:
    print("Вася")
else:
    print("Толя")
```

D. Список победителей
```python
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())
min_speed = min(petya_speed, vasya_speed, tolya_speed)
max_speed = max(petya_speed, vasya_speed, tolya_speed)
if petya_speed == max_speed:
    first = "Петя"
elif petya_speed == min_speed:
    third = "Петя"
else:
    second = "Петя"

if vasya_speed == max_speed:
    first = "Вася"
elif vasya_speed == min_speed:
    third = "Вася"
else:
    second = "Вася"

if tolya_speed == max_speed:
    first = "Толя"
elif tolya_speed == min_speed:
    third = "Толя"
else:
    second = "Толя"
print(f"1. {first}\n2. {second}\n3. {third}")
```

E. Яблоки
```python
first_count = 6 + int(input())
second_count = 12 + int(input())
if first_count > second_count:
    print("Петя")
else:
    print("Вася")
```

F. Сила прокрастинации
```python
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
```

G. А роза упала на лапу Азора
```python
n = int(input())
if n // 1000 == n % 10 and n // 100 % 10 == n // 10 % 10:
    print("YES")
else:
    print("NO")
```

H. Зайка — 1
```python
phrase = input()
if "зайка" in phrase:
    print("YES")
else:
    print("NO")
```

I. Первому игроку приготовиться
```python
name_1 = input()
name_2 = input()
name_3 = input()
print(min(name_1, name_2, name_3))
```

J. Лучшая защита — шифрование
```python
n = int(input())
sum_1_2 = n // 100 + n // 10 % 10
sum_2_3 = n // 10 % 10 + n % 10
print(max(sum_1_2, sum_2_3), min(sum_1_2, sum_2_3), sep="")
```

K. Красота спасёт мир
```python
n = int(input())
d_1 = n // 100
d_2 = n // 10 % 10
d_3 = n % 10
if (d_1 + d_2 + d_3) * 2 == (max(d_1, d_2, d_3) + min(d_1, d_2, d_3)) * 3:
    print("YES")
else:
    print("NO")
```

L. Музыкальный инструмент
```python
a = int(input())
b = int(input())
c = int(input())
if (a < b + c) and (b < a + c) and (c < a + b):
    print("YES")
else:
    print("NO")
```

M. Властелин Чисел: Братство общей цифры
```python
a = int(input())
b = int(input())
c = int(input())
if a % 10 == b % 10 and a % 10 == c % 10:
    print(a % 10)
else:
    print(a // 10)
```

N. Властелин Чисел: Две Башни
```python
n = int(input())
d_1 = n % 10
d_2 = n // 10 % 10
d_3 = n // 100
min_d = min(d_1, d_2, d_3)
max_d = max(d_1, d_2, d_3)
mid_d = d_1 + d_2 + d_3 - min_d - max_d
if min_d == 0:
    a = f"{mid_d}{min_d}"
else:
    a = f"{min_d}{mid_d}"
print(a, f"{max_d}{mid_d}")
```

O. Властелин Чисел: Возвращение Цезаря
```python
a = int(input())
b = int(input())
a_1 = a // 10
a_2 = a % 10
b_1 = b // 10
b_2 = b % 10
min_d = min(a_1, a_2, b_1, b_2)
max_d = max(a_1, a_2, b_1, b_2)
print(max_d, (a_1 + a_2 + b_1 + b_2 - min_d - max_d) % 10, min_d, sep="")
```

P. Легенды велогонок возвращаются: кто быстрее?
```python
petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

min_speed = min(petya_speed, vasya_speed, tolya_speed)
max_speed = max(petya_speed, vasya_speed, tolya_speed)

if petya_speed == max_speed:
    first = "Петя"
elif petya_speed == min_speed:
    third = "Петя"
else:
    second = "Петя"

if vasya_speed == max_speed:
    first = "Вася"
elif vasya_speed == min_speed:
    third = "Вася"
else:
    second = "Вася"

if tolya_speed == max_speed:
    first = "Толя"
elif tolya_speed == min_speed:
    third = "Толя"
else:
    second = "Толя"

print(f"{'': ^8}{first: ^8}{'': ^8}")
print(f"{second: ^8}{'': ^8}{'': ^8}")
print(f"{'': ^8}{'': ^8}{third: ^8}")
print(f"{'II': ^8}{'I': ^8}{'III': ^8}")
```

Q. Корень зла

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
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif (a == 0 and b == 0) or d < 0:
    print("No solution")
elif a == 0:
    root = -c / b
    print(f"{root:.2f}")
elif d == 0:
    root = -b / (2 * a)
    print(f"{root:.2f}")
else:
    root_1 = (-b - d ** 0.5) / (2 * a)
    root_2 = (-b + d ** 0.5) / (2 * a)
    print(f"{min(root_1, root_2):.2f}", f"{max(root_1, root_2):.2f}")
```

R. Территория зла
1. Найдем квадрат самой большой стороны (обозначим ее c).
2. Найдем сумму квадратов двух других сторон (обозначим их a и b).
3. Сравним эти значения:
    * Если c^2 < a^2 + b^2, то треугольник остроугольный.
    * Если c^2 > a^2 + b^2, то треугольник тупоугольный.
    * Если c^2 == a^2 + b^2, то треугольник прямоугольный.

```python
a = int(input()) ** 2
b = int(input()) ** 2
c = int(input()) ** 2
g = max(a, b, c)
if 2 * g < a + b + c:
    print("крайне мала")
elif 2 * g > a + b + c:
    print("велика")
else:
    print("100%")
```

S. Автоматизация безопасности
1. Квадратиная функция
    * $y = (x + 1)^2 - 9$ Если учитывать движение графика горизонтально и вертикально => $(x + 1)$  горизонтально влево на $1$, $-9$ вертикально вниз на $9$.
    * $y = 1/4*x^2 + 1/2*x - 35/4$ Если решать системой уравнений  $a*x^2 + b*x + c = y$
2. Окружность
    * $(x - xc)^2 + (y - yc)^2 <= R^2$
3. Линейная функция
    $y = k*x + b$, $k = \frac{y_2 - y_1}{x_2 - x_1}$

    Канонический вид:
    $$\frac{x - x_1}{x_2 - x_1} = \frac{y - y_1}{y_2 - y_1}$$

```python
x = float(input())
y = float(input())
if (x ** 2 + y ** 2) ** 0.5 > 10:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    if (x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5) \
            or (-4 <= x <= 0 and 0 <= y <= 5) \
            or (-7 <= x <= -4 and 0 <= y <= (x * 5 / 3 + 35 / 3)) \
            or (-7 <= x <= 5 and ((x + 1) ** 2) / 4 - 9 <= y <= 0):
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")
```

T. Зайка — 2
```python
line_1 = input()
line_2 = input()
line_3 = input()
query = "зайка"
result = ""
if query in line_1:
    result = line_1
if query in line_2 and (result == "" or line_2 < result):
    result = line_2
if query in line_3 and (result == "" or line_3 < result):
    result = line_3
print(result, len(result))
```