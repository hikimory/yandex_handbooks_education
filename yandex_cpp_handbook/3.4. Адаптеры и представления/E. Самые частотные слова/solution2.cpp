#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

int main() {
    size_t k;
    std::cin >> k;

    std::unordered_map<std::string, int> words;
    std::string word;
    while (std::cin >> word) {
        ++words[word];
    }

    using TPair = std::pair<int, std::string>;  // удобный псевдоним для типа

    std::priority_queue<TPair> pq;
    for (const auto& [word, freq] : words) {
        pq.push({-freq, word});  // нарочно кладём отрицательную частоту
        if (pq.size() > k) {
            pq.pop();  // выкидываем элемент с минимальной (то есть, максимальной отрицательной) частотой
        }
    }

    // Копируем элементы в вектор
    std::vector<TPair> top;
    top.reserve(k);

    while (!pq.empty()) {
        const auto& [freq, word] = pq.top();
        top.push_back({-freq, word});  // возвращаем настоящую частоту
        pq.pop();
    }

    // Переворачиваем вектор
    std::reverse(top.begin(), top.end());

    for (const auto& [freq, word] : top) {
        std::cout << word << "\t" << freq << "\n";
    }
}