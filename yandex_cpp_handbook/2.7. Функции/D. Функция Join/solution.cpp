#include <string>
#include <vector>

std::string Join(std::vector<std::string>& tokens, char delim) {
    std::string result;
    for (size_t i = 0; i != tokens.size(); ++i) {
        if (i > 0) {
            result += delim;
        }
        result += tokens[i];
    }
    return result;
}