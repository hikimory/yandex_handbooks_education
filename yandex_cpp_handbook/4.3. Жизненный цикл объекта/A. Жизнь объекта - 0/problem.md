# Жизнь объекта - 0
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

Вам дан готовый класс Logger, который в своих конструкторах, операторах присваивания и деструкторе печатает соответствующие сообщения:

```
#include <iostream>

class Logger {
private:
    static int counter;
    const int id;

public:
    Logger(): id(++counter) {
        std::cout << "Logger(): " << id << "\n";
    }

    Logger(const Logger& other): id(++counter) {
        std::cout << "Logger(const Logger&): " << id << " " << other.id << "\n";
    }

    Logger(Logger&& other): id(++counter) {
        std::cout << "Logger(Logger&&): " << id << " " << other.id << "\n";
    }

    Logger& operator = (const Logger& other) {
        std::cout << "Logger& operator = (const Logger&): " << id << " " << other.id << "\n";
        return *this;
    }

    Logger& operator = (Logger&& other) {
        std::cout << "Logger& operator = (Logger&&): " << id << " " << other.id << "\n";
        return *this;
    }

    ~Logger() {
        std::cout << "~Logger(): " << id << "\n";
    }
};

int Logger::counter = 0;
```

Вам требуется написать программу, которая работает с этим классом и выводит следующий текст:

Logger(): 1
~Logger(): 1
Logger(): 2
~Logger(): 2

## Примечание
Не вставляйте код класса в решение. Используйте вместо этого директиву #include "logger.h" в начале программы. Не пытайтесь вывести нужный текст с помощью непосредственной печати: мы при проверке всё равно заменяем отладочные сообщения в классе на свои.