#include <iostream>
#include <vector>
#include <stdexcept>


template <typename T>
class AdvancedVector {
public:
    using Container = typename std::vector<T>;
    using ConstIterator = typename Container::const_iterator;

    AdvancedVector() = default;
    AdvancedVector(const Container& data)
        : data{ data } {
    }

    template<typename ForwardIt>
    AdvancedVector(ForwardIt first, ForwardIt last)
        : data{ first, last } {
    }

    AdvancedVector<T>& operator = (const AdvancedVector<T>& other) {
        data.clear();
        for (size_t i = 0; i < other.size(); i++)
        {
            data.push_back(other[i]);
        }
        return *this;
    }

    const Container& GetData() const {
        return data;
    }

    bool empty() const {
        return data.size() == 0;
    }

    size_t size() const {
        return data.size();
    }

    void push_back(const T& value) {
        data.push_back(value);
    }

    void pop_back() {
        data.pop_back();
    }

    bool operator == (const AdvancedVector<T>& other) {
        return data == other.GetData();
    }

    bool operator != (const AdvancedVector<T>& other) {
        return !(data == other.GetData());
    }

    const T& operator [] (int idx) const {
        if (idx <  0)
            return data.at(data.size() + idx);
        else
            return data.at(idx);
    }

    T& operator [] (int idx) {
        if (idx < 0)
            return data.at(data.size() + idx);
        else
            return data.at(idx);
    }

private:
    Container data;
};


// using implementation
#include <cstdint>
#include <vector>

template <typename T>
class AdvancedVector: public std::vector<T> {
public:
    AdvancedVector() = default;

    template <typename Iter>
    AdvancedVector(Iter first, Iter last): std::vector<T>(first, last) {
    }

    const T& operator [](std::int64_t i) const {
        if (i < 0) {
            i += this->size();
        }
        return this->at(i);
    }

    T& operator [](std::int64_t i) {
        if (i < 0) {
            i += this->size();
        }
        return this->at(i);
    }
};