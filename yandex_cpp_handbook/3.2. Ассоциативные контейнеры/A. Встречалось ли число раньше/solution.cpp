#include <iostream>
#include <unordered_set>

int main() {
    std::unordered_set<int> numbers;
    int number;
    while (std::cin >> number) {
        if (numbers.insert(number).second) {
            std::cout << "NO\n";
        } else {
            std::cout << "YES\n";
        }
    }
}