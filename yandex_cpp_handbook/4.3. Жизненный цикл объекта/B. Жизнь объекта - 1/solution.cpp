#include "logger.h"

int main() {
    Logger logger1;
    Logger logger2(logger1);  //  Можно записать иначе: Logger logger2 = logger1;
}