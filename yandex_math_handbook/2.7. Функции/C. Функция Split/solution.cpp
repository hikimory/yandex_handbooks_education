#include <string>
#include <string_view>
#include <vector>

std::vector<std::string_view> Split(const std::string& s, char delimiter) {
    std::string_view str = s;
    std::vector<std::string_view> result;
    size_t i = 0;
    for (size_t j = 0; j != str.size(); ++j) {
        if (str[j] == delimiter) {
            result.push_back(str.substr(i, j - i));
            i = j + 1;
        }
    }
    result.push_back(str.substr(i));
    return result;
}