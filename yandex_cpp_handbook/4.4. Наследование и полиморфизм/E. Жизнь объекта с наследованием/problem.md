# Жизнь объекта с наследованием

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

Вам дан класс A, который в своих конструкторах и деструкторе печатает соответствующие сообщения, а так же main:

```
#include <iostream>

class A {
public:
    A(int x) {
        std::cout << "Constructor(int): " << x << "\n";
    }
    A(const A&) {
        std::cout << "Copy constructor\n";
    }
    virtual ~A() {
        std::cout << "Destructor\n";
    }
    virtual void foo() const = 0;
};

#include "your_code.h"

int main() {
    B b;
    const A& a = b;
    a.foo();
}
```

Вам требуется написать код класса B, чтобы функция main, работающая с этим классом, вывела бы следующие сообщения:

Constructor(int): 42
Destructor

## Примечание
Не пытайтесь вывести нужный текст с помощью непосредственной печати: мы при проверке всё равно заменяем отладочные сообщения в классе на свои.