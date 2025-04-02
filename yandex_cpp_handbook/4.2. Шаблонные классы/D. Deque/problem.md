# Deque

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

В этой задаче вам надо будет написать свой дек. Писать его по-честному долго и сложно, поэтому мы пошли вам навстречу: вам нужно написать упрощенную версию дека без итераторов, и умеющую только добавлять элементы в начало и конец. Поддерживать удаление элементов из дека не требуется.

В отличие от стандартного дека возьмите за основу два вектора, растущих каждый в свою сторону. Предлагаем такой прототип — а вам нужно реализовать указанные функции:

```cpp
#include <cstddef>
#include <vector>

template <typename T>
class Deque {
private:
    std::vector<T> head, tail;

public:
    bool Empty() const;

    size_t Size() const;

    void Clear();

    const T& operator [] (size_t i) const;

    T& operator [] (size_t i);

    const T& At(size_t i) const;  // throws std::out_of_range on incorrect index

    T& At(size_t i);  // throws std::out_of_range on incorrect index

    const T& Front() const;

    T& Front();

    const T& Back() const;

    T& Back();

    void PushFront(const T& elem);

    void PushBack(const T& elem);
};
```

## Примечание
Сдайте в систему класс Deque с написанными функциями.