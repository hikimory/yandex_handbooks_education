# Выполнение операций со списком

Изначально у вас есть пустой список. Далее вам поступает q запросов. Каждый запрос одного из следующих типов:

*   Запрос 1-ого типа: добавить число y после x\-ого числа в списке. Если $x\=0$, то нужно сделать число y новым началом списка
*   Запрос 2-ого типа: вывести число, которое находится на позиции x в списке
*   Запрос 3-его типа: удалить число, которое находится на позиции x в списке

После каждого запроса второго типа необходимо вывести число, являющееся ответом. Гарантируется, что в списке в этот момент находилось хотя бы x элементов.

Также гарантируется, что если вам поступил запрос первого или третьего типа, то список к этому моменту содержал хотя бы x элементов.

## Формат ввода

Первая строка содержит единственное число q -- количество запросов.

Далее следует q строк. Каждая из этих строк может иметь один из следующих видов:

*   Для запроса первого типа - "1 x y" (без кавычек)
*   Для запросов второго типа - "2 x" (без кавычек)
*   Для запросов третьего типа - "3 x" (без кавычек)

## Формат вывода

Вывод должен состоять из count строк, где count -- количество запросов второго типа. Каждая строка должна содержать ответ на соответствующий запрос в формате value (где value -- число, которое находится на позиции x).

## Пример

Ввод

    8
    1 0 5
    2 1
    3 1
    1 0 6
    1 0 7
    2 2
    1 1 5
    2 2
    

Вывод

    5
    6
    5
    

## Примечание

Пусть $size\_i$​ -- размер списка в момент i\-ого запроса.

Ограничения:

*   $1 \leq q \leq 5 \cdot 10^3$
*   Для запросов первого типа $0 \leq x \leq size\_i$​ и $1 \leq y \leq 10^6$.
*   Для запросов второго типа $1 \leq x \leq size\_i$​
*   Для запросов третьего типа $1 \leq x \leq size\_i$​

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
