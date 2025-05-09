# Ближайшие точки

Заданы n точек на плоскости.

Ваша задача - найти ближайшую пару точек из заданного множества.

## Формат ввода

Первая строка содержит n точек. Каждая из следующих n строк определяет точку $(x\_i,y\_i)$.

Ограничения: $2 \le n \le 10^5$; $-10^9 \le x\_i,y\_i \le 10^9$ -- целые числа.

## Формат вывода

Минимальное расстояние.

### Пример 1

Ввод

    2
    0 0
    3 4
    

Вывод

    5.000000
    

### Пример 2

Ввод

    11
    4 4
    -2 -2
    -3 -4
    -1 3
    2 3
    -4 0
    1 1
    -1 -1
    3 -1
    -4 2
    -2 4
    

Вывод

    1.414214
    

### Пример 3

Ввод

    3
    0 0
    1 1
    0 0
    

Вывод

    0.000000
    

## Примечание

Помните, что расстояние между точками $(x\_1,y\_1)$ и $(x\_2,y\_2)$ равно $\sqrt{(x\_1-x\_2)^2+(y\_1-y\_2)^2}$​. Так, хотя ввод и содержит только целые числа, ответ необязательно будет целым числом, и потому вам нужно обратить внимание на точность при выводе результатов.

Абсолютное значение разницы между ответом вашей программы и оптимальным значением не должно превышать $10^{-5}$. Для этого ваш ответ должен содержать не более и не менее шести значащих цифр в дробной части. Иначе даже правильно вычисленный результат может не пройти нашу систему проверки из-за ошибок при округлении. Незначащие нули на проверку не влияют.

<table>
 <tr class="time-limit">
    <td class="property-title">Ограничение времени</td>
    <td>1&nbsp;секунда</td>
 </tr>
 <tr class="memory-limit">
    <td class="property-title">Ограничение памяти</td>
    <td>256.0Mb</td>
 </tr>
 <tr class="input-file">
    <td class="property-title">Ввод</td>
    <td colspan="1">стандартный ввод или input.txt</td>
 </tr>
 <tr class="output-file">
    <td class="property-title">Вывод</td>
    <td colspan="1">стандартный вывод или output.txt</td>
 </tr>
</table>
