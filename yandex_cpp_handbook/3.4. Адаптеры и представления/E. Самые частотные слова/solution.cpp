#include <algorithm>
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

int main() {
    size_t k;
    std::cin >> k;

    // Подсчитываем частоты слов
    std::unordered_map<std::string, int> words;
    std::string word;
    while (std::cin >> word) {
        ++words[word];
    }

    // Переносим слова и их частоты в вектор
    std::vector<std::pair<std::string, int>> v(words.begin(), words.end());

    // Находим максимальные k элементов
    std::partial_sort(
        v.begin(),
        v.begin() + std::min(v.size(), k),  // k может оказаться больше размера вектора
        v.end(),
        [](const auto& p1, const auto& p2) { return std::tie(p2.second, p1.first) < std::tie(p1.second, p2.first); }
    );

    // Печатаем топовые слова
    for (size_t i = 0; i < k && i < v.size(); ++i) {
        const auto& [word, freq] = v[i];
        std::cout << word << "\t" << freq << "\n";
    }
}