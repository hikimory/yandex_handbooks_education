#include <iostream>
#include <deque>
#include <string>

int main() {
    std::deque<std::string> works;

    int n = 0;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        std::string name, position;
        std::cin >> name >> position;

        if (position == "top") {
            works.push_front(name);
        } else {
            works.push_back(name);
        }
    }

    int k = 0;
    std::cin >> k;
    for (int i = 0; i < k; ++i) {
        int x = 0;
        std::cin >> x;
        std::cout << works[x - 1] << "\n";
    }
}