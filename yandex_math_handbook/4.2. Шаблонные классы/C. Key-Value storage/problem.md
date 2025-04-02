# Key-Value storage

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

Вася разрабатывает свою структуру — базу данных «ключ-значение». Эта структура данных должна хранить значение, ассоциированное с ключом, и она будет делать это суперэффективно. Пока для простоты Вася выбрал за основу ```std::unordered_map```, но потом он это переделает.

Какие операции должно поддерживать такое хранилище? Правильно: вставка элемента, удаление элемента и поиск элемента. Вася написал прототипы функций Insert, Remove и Find, но функция Find почему-то не работает. Помогите Васе её исправить. Вот код Васи:

```
#include <unordered_map>

template <typename Key, typename Value>
class KeyValueStorage {
private:
      std::unordered_map<Key, Value> data;

public:
    void Insert(const Key& key, const Value& value) {
        data[key] = value;
    }

    void Remove(const Key& key) {
        data.erase(key);
    }

    bool Find(const Key& key, Value* const value = nullptr) const;
};


// Почему-то не работает...
//
// template <typename Key, typename Value>
// bool KeyValueStorage<Key, Value>::Find(const Key& key, Value* const value) const {
//     auto it = std::find(data.begin(), data.end(), key);
//     auto val = *it;
//     if (value != nullptr)
//         value = &val;
//     return it != data.end();
// }

// Ваша реализация функции KeyValueStorage::find будет вставлена сюда:
#include "your_version_of_find.h"
```
Ваша версия функции Find будет вставлена в конце этого кода. Её заголовок должен быть таким же, как в закомментированной части.

Функция Find по задумке должна возвращать true, если ключ был найден, и false в противном случае. Если второй аргумент функции Find отличен от nullptr и ключ найден, то функция должна записать найденное значение в тот объект, на который ссылается этот аргумент (предполагается, что новая структура данных сможет быстро определять наличие ключа, но само значение будет извлекаться дорого, и делать это нужно лишь при необходимости). Использовать эту функцию предполагается примерно так:

```
#include "key_value_storage.h"

#include <string>

int main() {
    KeyValueStorage<std::string, int> kv;
    kv.Insert("hello", 42);
    kv.Insert("bye", -13);
    int value = 123;
    auto res = kv.Find("wrong", &value);  // должно вернуться false, а value не должен меняться
    res = kv.Find("bye", &value);  // должно вернуться true, в value должно быть -13
    res = kv.Find("hello", nullptr);  // должно вернуться true
}
```