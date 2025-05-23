# AdvancedVector

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

Реализуйте класс AdvancedVector. Продвинутый вектор отличается от обычного тем, что позволяет обращаться по отрицательным индексам к элементам вектора в обратном порядке ( прямо как в Python). Например, vec[-1] возвращает последний элемент, vec[-2] возвращает предпоследний и так далее.

Класс AdvancedVector должен хранить элементы шаблонного типа T. Требуемый функционал не сильно отличается от стандартного std::vector:

Класс должен называться AdvancedVector.

1. У класса должен быть шаблонный параметр T — тип элементов.

2. У класса должен быть конструктор по умолчанию.

3. У класса должен быть конструктор копирования (возможно, предоставленный компилятором).

4. У класса должен быть шаблонный конструктор, принимающий два итератора и заполняющий вектор из данного диапазона.

5. У класса должен быть оператор присваивания (возможно, предоставленный компилятором).

6. У класса должны быть операторы сравнения == и !=.

7. У класса должны быть константные функции empty() и size().

8. У класса должны быть функции pop_back() и push_back(const T&).

9. У класса должны быть константная и неконстантная версии оператора [].

В случае положительного индекса нужно вернуть элемент с соответствующим индексом, если он меньше размера вектора. Иначе нужно бросить исключение std::out_of_range. В случае отрицательного индекса нужно вернуть элемент с соответствующим индексом, предполагая, что последний элемент имеет номер −1, предпоследний −2 и так далее. Но только пока модуль индекса не превосходит size(). Если же std::abs(index) > size, то нужно бросить исключение std::out_of_range.

Формат ввода
Гарантируется, что передаваемый в operator [] индекс лежит в отрезке 
$[−10^9;10^9]$.

## Примечание
Сдайте в систему только код класса AdvancedVector без функции main. Подключите все необходимые для вашей реализации библиотеки.