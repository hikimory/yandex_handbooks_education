# Поиск доминирующего элемента

Ваша задача - проверить, содержит ли данная последовательность элемент, который встречается более половины раз.

## Формат ввода

Первая строка содержит целое число n, следующая - последовательность nnn целых неотрицательных чисел $a\_0, \dotsc, a\_{n-1}$​.

Ограничения: $1 \le n \le 10^5$; $0 \le a\_i \le 10^9$ для всех $0 \le i \lt n$.

## Формат вывода

Выведите 1, если в последовательности содержится элемент, который встречается больше, чем _n/2_ раз, и 0 в противном случае.

### Пример 1

Ввод

    5
    2 3 9 2 2
    

Вывод

    1
    

### Пример 2

Ввод

    4
    1 2 3 1
    

Вывод

    0
    

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
