# Минимальная длина покрывающих отрезков

Заданы n точек на координатной прямой. Вам требуется покрыть все точки на прямой k отрезками одинаковой длины.

Необходимо определить, какую минимальную длину могут иметь отрезки.

## Формат ввода

В первой строке находится два разделенных пробелом числа n,k $(1 \leq n, k \leq 10^5$.

Во второй строке заданы координаты n точек $x\_i$​ $(1 \leq x\_i \leq 10^9)$.

## Формат вывода

Вывод должен состоять из одного числа -- минимальная длина отрезков.

### Пример 1

Ввод

    5 3
    2 3 9 11 20
    

Вывод

    2
    

### Пример 2

Ввод

    5 2
    2 3 9 11 20
    

Вывод

    9
    

### Пример 3

Ввод

    4 2
    1 2 1 2
    

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
