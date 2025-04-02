#include <map>
#include <memory>
#include <optional>
#include <stdexcept>

template <typename Key1, typename Key2, typename Value>
class BiMap {
private:
    std::map<Key1, std::shared_ptr<Value>> map1;
    std::map<Key2, std::shared_ptr<Value>> map2;

public:
    void Insert(
        const std::optional<Key1>& key1,
        const std::optional<Key2>& key2,
        const Value& value
    ) {
        if (!key1.has_value() && !key2.has_value()) {
            throw std::invalid_argument("Both keys are empty");
        }

        auto shared = std::make_shared<Value>(value);

        if (key1.has_value() && map1.find(*key1) != map1.end()) {
            throw std::invalid_argument("Key already exists");
        }

        if (key2.has_value() && map2.find(*key2) != map2.end()) {
            throw std::invalid_argument("Key already exists");
        }

        if (key1.has_value()) {
            map1[*key1] = shared;
        }

        if (key2.has_value()) {
            map2[*key2] = shared;
        }
    }

    Value& GetByPrimaryKey(const Key1& key) {
        return *map1.at(key);
    }

    const Value& GetByPrimaryKey(const Key1& key) const {
        return *map1.at(key);
    }

    Value& GetBySecondaryKey(const Key2& key) {
        return *map2.at(key);
    }

    const Value& GetBySecondaryKey(const Key2& key) const {
        return *map2.at(key);
    }
};