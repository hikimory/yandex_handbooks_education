#include <vector>
#include <algorithm>

template <typename T>
void Duplicate(std::vector<T>& v) {
    for (size_t n = v.size(), i = 0; i < n; ++i) {
        v.push_back(v[i]);
    }
}

// version2

template <typename T>
void Duplicate(std::vector<T>& v) {
    v.reserve(v.size() * 2);
    std::copy(v.begin(), v.end(), std::back_inserter(v));
}