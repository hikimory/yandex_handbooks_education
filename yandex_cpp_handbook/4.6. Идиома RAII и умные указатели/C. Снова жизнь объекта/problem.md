# Снова жизнь объекта

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

Вам дан класс A и функция main():

```cpp
#include <iostream>
#include <memory>

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
    virtual void foo() const {
        std::cout << "A::foo()\n";
    }
};

#include "your_code.h"

int main() {
    std::unique_ptr<A> ptr(new B);
    ptr->foo();
}
```

Напишите такой код класса B, чтобы функция main() вывела бы сообщения:

Constructor(int): 42
Constructor(int): 17
A::foo()
Destructor
Destructor

## Примечание
Не пытайтесь вывести нужный текст с помощью непосредственной печати: мы при проверке всё равно заменяем отладочные сообщения в классе на свои.