# Перепад цен

Дан массив a, состоящий из n чисел. Необходимо найти две пары индексов $i\_1 < j\_1$​ и $i\_2 < j\_2$​ таких, что $a\_{i\_1} - a\_{j\_1}$​​ минимально возможное и $a\_{i\_2} - a\_{j\_2}$​ максимально возможное.

## Формат ввода

Первая строка содержит единственное число n - количество чисел в массиве.

Вторая строка содержит n разделенных пробелом чисел $a\_i$​, где $a\_i$​ -- число на i\-ой позиции в массиве a.

## Формат вывода

Первая строка вывода должна содержать два разделенных пробелом числа $i\_1$​ и $j\_1$​. Если подходящих пар несколько, то нужно выбрать пару с минимальным значеним $i\_1$​. Если пар с минимальным значением $i\_1$​ несколько, то нужно выбрать пару с минимальным значеним $j\_1$​.

Вторая строка вывода должна содержать два разделенных пробелом числа $i\_2$ и $j\_2$​. Если подходящих пар несколько, то нужно выбрать пару с минимальным значеним $i\_2$​. Если пар с минимальным значением $i\_2$​ несколько, то нужно выбрать пару с минимальным значеним $j\_2$​.

### Пример 1

Ввод

    6
    2 1 3 5 2 4
    

Вывод

    2 4
    4 5
    

### Пример 2

Ввод

    5
    3 2 4 5 6
    

Вывод

    2 5
    1 2
    

## Примечание

Ограничения:

*   $3 \le n \le 10^5$
*   $1 \le a\_i \le 10^5$ для всех $1 \le i \le n$

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
