#include <iostream>

int main() {
    int month, year;
    std::cin >> month >> year;

    switch (month) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            std::cout << "31" << std::endl;
            break;
        case 2:
            if ((year % 400 == 0 || year % 100 != 0) && year % 4 == 0) {
                std::cout << "29" << std::endl;
            } else {
                std::cout << "28" << std::endl;
            }
            break;
        default:
            std::cout << "30" << std::endl;
    }
}