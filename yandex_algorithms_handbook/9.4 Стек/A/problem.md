# Выполнение операций со стеком

Изначально у вас есть пустой стек. Далее вам поступает q запросов. Каждый запрос одного из следующих типов:

*   Запрос 1-ого типа: положить число xxx на вершину стека
*   Запрос 2-ого типа: достать число, лежащее на вершине стека

После каждого запроса необходимо вывести число, которое лежит на вершине стека. Если стек пустой, то выведите −1.

Также гарантируется, что если вам поступил запрос второго типа, то стек к этому моменту не был пустым.

## Формат ввода

Первая строка содержит единственное число q -- количество запросов.

Далее следует q строк. Каждая из этих строк может иметь один из следующих видов:

*   Для запроса первого типа - "1 x" (без кавычек).
*   Для запросов второго типа - "2" (без кавычек).

## Формат вывода

Вывод должен состоять из q строк. Каждая строка должна содержать ответ на соответствующий запрос в формате top (где top - число, которое лежало на вершине стека), либо −1, если стек был пустым.

## Пример

Ввод

    5
    1 5
    2
    1 6
    1 7
    2
    

Вывод

    5
    -1
    6
    7
    6
    

## Примечание

Ограничения:

*   $1 \leq q \leq 10^6$
*   Во всех запросах первого типа выполнено $1 \leq x \leq 10^6$


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
