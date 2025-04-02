#include <iostream>

int main() {
    double centimeters;
    std::cin >> centimeters;
    double inches = centimeters / 2.54;
    std::cout << inches << std::endl;
}