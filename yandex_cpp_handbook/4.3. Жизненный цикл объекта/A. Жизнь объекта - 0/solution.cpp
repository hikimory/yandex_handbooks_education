#include "logger.h"

int main(){
    {Logger x;}
    {Logger y;}
}

void CreateLogger() {
    Logger logger;
}

int main2() {
    CreateLogger();
    CreateLogger();
}