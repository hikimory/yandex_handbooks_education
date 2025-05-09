# Адреса
<table>
 <tr>
    <td>Ограничение времени</td>
    <td>2 c</td>
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

Алексею поручили написать программу, обрабатывающую почтовые адреса.

Дана структура Address и несколько работающих с ней функций:
```
#pragma once

#include <string>

struct Address {
    std::string Country;
    std::string City;
    std::string Street;
    std::string House;
};

void Parse(const std::string& line, Address* const address);
void Unify(Address* const address);
std::string Format(const Address& address);
```

Функция Parse принимает на вход текстовую строчку и пытается выделить из неё компоненты адреса.

Функция Unify пытается привести компоненты адреса к каноническому виду (например, вместо «пр-д Кочновский» записать «Кочновский проезд»).

Функция Format возвращает текстовое представление адреса.

Функции Parse и Unify, в духе Google C++ style guide, принимают на вход изменяемые параметры через указатели. Предполагается, что соотвествующие объекты типа Address уже созданы.

В случае ошибок обработки адреса функции Parse и Unify могут сгенерировать исключения.

Алексей написал код обработки, но он почему-то не работает:

```
#include "address.h"
#include <iostream>
#include <string>

int main() {
    std::string line;
    Address* address;
    while (getline(std::cin, line)) {
        Parse(line, address);
        Unify(address);
        std::cout << Format(*address) << "\n";
    }
}
```

Предполагалось, что эта программа будет читать поступающие на вход строки, извлекать из них адреса и печатать их обработанные текстовые представления. В случае исключений при обработке строки программа должна напечатать просто “exception” (с переводом строки) и перейти к обработке следующих строк.

## Примечание
Вам нужно исправить ошибки в коде и сдать его в систему. Код структуры Address и функций переписывать не надо: просто подключите в своей программе заголовочный файл address.h. Утечек памяти в вашей программе быть не должно.