# TimerGuard

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

Вася хочет замерять время работы разных частей своей программы. Сейчас он делает это средствами стандартной библиотеки так:

```
#include <iostream>
#include <chrono>

#include "some_long_stuff.h"

void SomeFunc() {
    auto start1 = std::chrono::high_resolution_clock::now();
    FirstLongFunction();
    std::chrono::duration<double> diff1 = std::chrono::high_resolution_clock::now() - start1;
    std::cout << "FirstLongFunction elapsed: " << diff1.count() << "\n";

    auto start2 = std::chrono::high_resolution_clock::now();
    SecondLongFunction();
    std::chrono::duration<double> diff2 = std::chrono::high_resolution_clock::now() - start2;
    std::cout << "SecondLongFunction elapsed: " << diff2.count() << "\n";

    auto start3 = std::chrono::high_resolution_clock::now();
    ThirdLongFunction();
    std::chrono::duration<double> diff3 = std::chrono::high_resolution_clock::now() - start3;
    std::cout << "ThirdLongFunction elapsed: " << diff3.count() << "\n";
}

int main() {
    SomeFunc();
    return 0;
}
```
Но ему очень не удобно каждый раз прописывать начало замера и конец. Помогите ему сделать это удобнее.

Напишите обёртку TimerGuard. Это класс, который создается перед началом вычислений и при выходе из своего scope пишет в поток время работы, которое он существовал. С его помощью Вася сможет писать так:

```
#include <iostream>
#include <chrono>

#include "some_long_stuff.h"

void SomeFunc() {
    {
        TimerGuard timer("FirstLongFunction elapsed: ", std::cout);
        FirstLongFunction();
    }
    {
        TimerGuard timer("SecondLongFunction elapsed: ", std::cout);
        SecondLongFunction();
    }
    {
        TimerGuard timer("ThirdLongFunction elapsed: ", std::cout);
        ThirdLongFunction();
    }
}

int main() {
    SomeFunc();
    return 0;
}
```

Класс TimerGuard должен содержать следующий конструктор:

TimerGuard(std::string message = "", std::ostream& out = std::cout);

message — сообщение, печатаемое перед перед временем. out — поток, в который нужно печатать сообщение.

Деструктор класса должен печатать сообщение в формате "{message} {time}" (обратите внимание на пробел).

## Примечание
Сдайте в систему только код конструкции TimerGuard без функции main. Подключите необходимые библиотеки.

Обратите внимание, что данный guard очень полезен даже вне этой задачи. Его можно использовать при отладке медленных участков вашей программы!