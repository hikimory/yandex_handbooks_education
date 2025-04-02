#include <iostream>

int main() {
    int number;
    std::cin >> number;

    int sum = 0;
    while(number > 0){
        sum += num % 10;
        num /= 10;
    }

    std::cout << sum << std::endl;
}


// version 2
// #include <iostream>
// #include <string>

// int main() {
//     std::string digits;
//     std::cin >> digits;

//     int s = 0;
//     for (char digit : digits) {
//         s += digit - '0';
//     }

//     std::cout << s << "\n";
// }