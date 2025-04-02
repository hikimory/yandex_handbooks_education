#include <cstdint>
#include <iostream>

int main() {
    std::uint64_t number = 0;
    std::cin >> number;

    if (number % 2 == 0) {
        std::cout << (number / 2) * (number + 1);
    } else {
        std::cout << ((number + 1) / 2) * number;
    }
    std::cout << "\n";
}