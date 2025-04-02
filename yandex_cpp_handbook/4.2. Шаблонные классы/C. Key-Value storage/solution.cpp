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
template <typename Key, typename Value>
bool KeyValueStorage<Key, Value>::Find_Wrong(const Key& key, Value* const value) const {
    auto it = std::find(data.begin(), data.end(), key);
    auto val = *it;
    if (value != nullptr)
        value = &val;
    return it != data.end();
}

// Не надо пытаться использовать общий алгоритм std::find или std::find_if. 
// Нужно использовать встроенную функцию find контейнера unordered_map. 
// Во-первых, встроенный find будет работать быстрее (а std::find будет выполнять линейный поиск). 
// Во-вторых, std::find не предназначен для поиска по ключу. 
// Он ищет в контейнере готовый образец, а значит, ему придётся передать пару из ключа и значения (которого мы не знаем).

// Если значение не найдено, не надо ничего делать с value. 
// Это можно понять по примеру использования. 
// В этом случае надо просто вернуть false.

// Неправильно писать value = &it->second. 
// Сам указатель value мы поменять не сможем; мы лишь записываем найденное значение в ту ячейку памяти, 
// на которую он указывает (если он не nullptr). 
// По условию мы предполагаем, что он в таком случае указывает на корректный существующий объект.

template <typename Key, typename Value>
bool KeyValueStorage<Key, Value>::Find(const Key& key, Value* const value) const {
    auto it = data.find(key);
    if (it != data.end() && value != nullptr) {
        *value = it->second;
    }
    return it != data.end();
}