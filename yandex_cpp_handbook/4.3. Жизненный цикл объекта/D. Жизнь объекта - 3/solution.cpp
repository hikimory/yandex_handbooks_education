#include <utility>
#include "logger.h"

int main() {
    Logger logger1, logger2;
    logger1 = logger2;
    logger1 = std::move(logger2);
}