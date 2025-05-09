# Выполнение операций со словарем

Изначально у вас есть пустой словарь. Далее вам поступает q запросов. Каждый запрос одного из следующих типов:

*   Запрос 1-ого типа: поставить в соответствие ключу x число y
*   Запрос 2-ого типа: проверить, какое число соответствует ключу x.

Считайте, что изначально каждому ключу соответствует число −1.

## Формат ввода

Первая строка содержит единственное число q -- количество запросов.

Далее следует q строк. Каждая из этих строк может иметь один из следующих видов:

*   Для запроса первого типа - "1 x y" (без кавычек).
*   Для запроса второго типа - "2 x" (без кавычек).

## Формат вывода

Вывод должен состоять из count строк, где count -- количество запросов второго типа. Каждая строка должна содержать одно число, которое соответствует ключу.

## Пример

Ввод

    9
    1 2 3
    2 1
    2 2
    1 1 4
    2 1
    2 2
    1 2 5
    2 1
    2 2
    

Вывод

    -1
    3
    4
    3
    4
    5
    

## Примечание

Ограничения:

*   $1 \leq q \leq 1 \cdot 10^5$
*   Для запросов первого типа выполнено $1 \leq x, y \leq 10^9$
*   Для запросов второго типа выполнено $1 \leq x \leq 10^9$


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
