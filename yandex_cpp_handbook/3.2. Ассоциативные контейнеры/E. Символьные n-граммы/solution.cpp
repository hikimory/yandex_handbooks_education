#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

int main() {
    size_t m, n;
    std::cin >> m >> n;

    std::unordered_map<std::string, int> freqs;

    for (size_t i = 0; i != m; ++i) {
        std::string word;
        std::cin >> word;
        for (size_t j = n; j <= word.size(); ++j) {
            ++freqs[word.substr(j - n, n)];
        }
    }

    std::vector<std::pair<std::string, int>> sorted(freqs.begin(), freqs.end());
    std::sort(
        sorted.begin(),
        sorted.end(),
        [](const auto& p1, const auto& p2) {
            return std::tie(p2.second, p1.first) < std::tie(p1.second, p2.first);
        }
    );

    for (const auto& [word, freq] : sorted) {
        std::cout << word << " - " << freq << "\n";
    }
}