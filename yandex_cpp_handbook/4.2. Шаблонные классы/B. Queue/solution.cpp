#include <deque>

template <typename T, typename Container = std::deque<T>>
class Queue {
private:
    Container data;

public:
    const T& front() const {
        return data.front();
    }

    T& front() {
        return data.front();
    }

    void push(const T& elem) {
        data.push_back(elem);
    }

    void pop() {
        data.pop_front();
    }

    size_t size() const {
        return data.size();
    }

    bool empty() const {
        return data.empty();
    }

    bool operator == (const Queue& other) const {
        return data == other.data;
    }

    bool operator != (const Queue& other) const {
        return !operator==(other);
    }
};