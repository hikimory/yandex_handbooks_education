# Сортировка по убыванию

<table>
 <tr>
    <td>Ограничение времени</td>
    <td>1 c</td>
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

Вам даны строки текстового файла. Отсортируйте набор этих строк по убыванию.

## Формат ввода

Количество строк не превосходит 1000. Каждая строка состоит из символов ASCII с кодами от 32 до 126, длина строки не превосходит 100.

## Формат вывода

Напечатайте строки в отсортированном по убыванию порядке. Для сравнения строк друг с другом достаточно использовать стандартные операторы сравнения, определённые для std::string.

## Примечание

Компилятор не поддерживает std::ranges.

### Пример

Ввод

      one
      two
      three
            

Вывод

      two
      three
      one
