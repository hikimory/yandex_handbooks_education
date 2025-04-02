#include <iostream>
#include <list>

#include "logger.h"

int main() {
    size_t n = 0;
    std::cin >> n;

    std::list<Logger> loggers(n);
    for (size_t i = 0; i != n; ++i) {
        loggers.pop_front();
    }
}