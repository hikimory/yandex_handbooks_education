#include <algorithm>
#include <string>
#include <vector>

std::string CommonPrefix(const std::vector<std::string>& words) {
    if (words.empty()) {
        return {};
    }

    size_t minLen = words[0].size();
    for (const auto& word : words) {
        minLen = std::min(minLen, word.size());
    }

    for (size_t i = 0; i < minLen; ++i) {
        const char c = words[0][i];
        for (const auto& word : words) {
            if (word[i] != c) {
                return word.substr(0, i);
            }
        }
    }

    return words[0].substr(0, minLen);
}

// #include <string>
// #include <string_view>
// #include <vector>

// std::string_view CommonPrefix(const std::string_view a, const std::string_view b) {
//     size_t i = 0;
//     while (i != a.size() && i != b.size() && a[i] == b[i]) {
//         ++i;
//     }
//     return a.substr(0, i);
// }

// std::string CommonPrefix(const std::vector<std::string>& words) {
//     if (words.empty()) {
//         return {};
//     }
//     std::string_view prefix = words[0];
//     for (size_t i = 1; i != words.size() && !prefix.empty(); ++i) {
//         prefix = CommonPrefix(prefix, words[i]);
//     }
//     return std::string(prefix);
// }