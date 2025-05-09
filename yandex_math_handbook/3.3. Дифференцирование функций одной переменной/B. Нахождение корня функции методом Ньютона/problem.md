# Нахождение корня функции методом Ньютона

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>2 c</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64 Mb</td>
 </tr>
  <tr>
    <td>Ввод</td>
    <td>стандартный ввод или input.txt</td>
 </tr>
  <tr>
    <td>Вывод</td>
    <td>стандартный ввод или input.txt</td>
 </tr>
</table>

Вам дана полиномиальная функция одной переменной степени не выше второй:
$$f(x)=ax^2+bx+c,$$

а также начальное приближение x0 и допустимая погрешность $ε$. Требуется реализовать метод Ньютона для нахождения корня функции $f(x)$, начиная с точки $x0$.

Метод Ньютона основан на итерационной формуле:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

Необходимо найти корень x, для которого $∣f(x)∣<ε$, или определить, что решение не может быть найдено за 1000 итераций.

## Важно

В этой задаче функция $f(x)$ является квадратичной, что позволяет нам вычислять производную $f′(x)$ аналитически без использования сторонних библиотек.

## Формат ввода

* Первая строка: три вещественных числа $a, b, c,$ разделённые пробелом — коэффициенты функции.
* Вторая строка: вещественное число $x_{0}$ — начальное приближение.
* Третья строка: вещественное число $ε$ — допустимая погрешность.

## Формат вывода

Если корень найден за не более чем 1000 итераций, выведите:

* Первая строка: Root found: x = ..., где x — найденный корень, округлённый до 6 знаков после запятой.
* Вторая строка: Number of iterations: ..., где указывается количество итераций, затраченных на поиск корня.

Если метод не сходится за 1000 итераций или если производная обращается в ноль в процессе вычислений, выведите:

```
Solution not found
```

## Ограничения

* $a,b,c,x0$ — вещественные числа, $a≠0$.
* $10^{-6}$.
* Максимальное количество итераций: 1000
* Функция $f(x)$ корректно задана и не содержит синтаксических ошибок.

## Пояснение к примерам:

Функция $f(x)=x^2−2x−3$ имеет корни в $x=−1$ и $x=3$.
Начальное приближение $x_{0}=4.0$ сходится к корню $x=3$ за 4 итерации с заданной точностью.

### Пример

Ввод
```
1 -2 -3
4
1e-6
```

Вывод
```
Root found: x = 3.000000
Number of iterations: 4
```