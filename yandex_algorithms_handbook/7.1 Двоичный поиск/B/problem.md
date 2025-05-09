# Множественный поиск ключей в отсортированной последовательности

Ваша задача --- для m значений $q\_i$​ необходимо проверить, входит ли $q\_i$​ в K.

## Формат ввода

Отсортированный массив K неповторяющихся целых чисел и массив целых чисел ***Q***$[q\_0, \dotsc,q\_{m-1}]$.

Первые две строки ввода содержат целое число n и последовательность $k\_0 \lt k\_1\lt \dotsc \lt k\_{n-1}$​ из n неповторяющихся положительных целых чисел в возрастающем порядке.

Следующие две строки содержат целое число m и m положительных целых чисел $q\_0, q\_1, \dotsc, q\_{m-1}$​.

Ограничения: $1 \le n \le 3 \cdot 10^4$; $1 \le m \le 10^5$; $1 \le k\_i \le 10^9$ для всех $0 \le i \lt n$; $1 \le q\_j \le 10^9$ для всех $0 \le j \lt m$.

## Формат вывода

Для всех i от 0 до m−1 выведите индекс $0 \le j \le n-1$, чтобы $k\_j=q\_i$​ или −1 при отсутствии такого индекса.

### Пример 1

Ввод

    7
    1 3 7 8 9 12 15
    1
    8
    

Вывод

    3
    

### Пример 2

Ввод

    7
    1 3 7 8 9 12 15
    3
    1 12 3
    

Вывод

    0
    5
    1
    

### Пример 3

Ввод

    2
    1 1000000000
    3
    1000000000 54321 1
    

Вывод

    1
    -1
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
