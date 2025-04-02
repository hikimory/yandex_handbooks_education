#include <iostream>
#include <map>
#include <set>
#include <string>

int main() {
    std::map<int, std::set<std::string>> index;

    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        std::string word;
        int page;
        std::cin >> word >> page;
        index[page].insert(word);
    }

    for (const auto& [page, words] : index) {
        std::cout << page;
        for (const auto& word : words) {
            std::cout << " " << word;
        }
        std::cout << "\n";
    }
}