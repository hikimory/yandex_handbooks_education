# Soundex

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

Известный алгоритм Soundex определяет, похожи ли два английских слова по звучанию. На вход он принимает слово и заменяет его на некоторый четырёхсимвольный код. Если коды двух слов совпадают, то слова, как правило, звучат похоже.

Вам требуется реализовать этот алгоритм. Он работает так:

1. Первая буква слова сохраняется.
2. В остальной части слова буквы a, e, h, i, o, u, w и y удаляются;
3. Оставшиеся буквы заменяются на цифры от 1 до 6, причём похожим по звучанию буквам соответствуют одинаковые цифры:

      * b, f, p, v: 1
      * c, g, j, k, q, s, x, z: 2
      * d, t: 3
      * l: 4
      * m, n: 5
      * r: 6

4. Любая последовательность идущих подряд одинаковых цифр сокращается до одной такой цифры.
5. Итоговая строка обрезается до первых четырёх символов.
6. Если длина строки получилась меньше четырёх символов, в конце добавляются нули.

Примеры:

ammonium → ammnm → a5555 → a5 → a500.
implementation → implmnttn → i51455335 → i514535 → i514.

## Формат ввода

На вход подаётся одно непустое слово из строчных латинских букв. Длина слова не превосходит 20 символов.

## Формат вывода

Напечатайте четырёхбуквенный код, соответствующий слову.