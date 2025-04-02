#include <iostream>
#include <map>
#include <set>
#include <string>

int main() {
    std::map<char, int> counter;
    std::string word;
    int wordsCount = 0;
    while (std::cin >> word) {
        ++wordsCount;
        std::set<char> letters(word.begin(), word.end());
        for (char c : letters) {
            ++counter[c];
        }
    }
    for (auto [c, freq] : counter) {
        if (freq == wordsCount) {
            std::cout << c;
        }
    }
    std::cout << "\n";
}