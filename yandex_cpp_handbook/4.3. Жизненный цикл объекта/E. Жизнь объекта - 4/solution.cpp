#include "logger.h"
#include <list>

int main() {
    Logger logger1;
    Logger* logger2 = new Logger;
    Logger* logger3 = new Logger;
    delete logger2;
    delete logger3;
}

int main2() {
    Logger logger1;  // создаём первый объект
    std::list<Logger> loggers(2);  // создаём 2 и 3 объекты
    loggers.pop_front();  // уничтожаем второй объект
}