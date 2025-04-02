#include <vector>
#include <utility>

template <typename T>
class Table {
private:
    std::vector<std::vector<T>> data;

public:
    Table(size_t m, size_t n) {
        resize(m, n);
    }

    // версия для неконстантных таблиц
    std::vector<T>& operator [] (size_t i) {
        return data[i];
    }

    // версия для константных таблиц
    const std::vector<T>& operator [] (size_t i) const {
        return data[i];
    }

    void resize(size_t m, size_t n) {
        data.resize(m);
        for (size_t i = 0; i < m; ++i) {
            data[i].resize(n);
        }
    }

    std::pair<size_t, size_t> size() const {
        if (data.empty()) {
            return {0, 0};
        } else {
            return {data.size(), data[0].size()};
        }
    }
};