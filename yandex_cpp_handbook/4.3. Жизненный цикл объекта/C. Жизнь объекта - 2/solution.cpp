#include <utility>
#include "logger.h"

int main() {
    Logger logger1;
    Logger logger2(std::move(logger1));  //  Можно записать иначе: Logger logger2 = std::move(logger1)
}