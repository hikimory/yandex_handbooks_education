#include <iostream>
#include <vector>

#include "logger.h"

int main() {
    size_t n = 0;
    std::cin >> n;

    std::vector<Logger> loggers(n);
    for (size_t i = 0; i != n; ++i) {
        loggers.pop_back();
    }
}