#include <iostream>
#include <string>
#include <vector>

int main() {
    std::string s;
    std::getline(std::cin, s);

    int i = 0;
    int j = static_cast<int>(s.size()) - 1;
    bool isPalindrome = true;

     while (i < j) {
        if (s[i] == ' ') {
            ++i;
        } else if (s[j] == ' ') {
            --j;
        } else if (s[i] != s[j]) {
            isPalindrome = false;
            break;
        } else {
            ++i;
            --j;
        }
    }

    if (isPalindrome) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }

    // version 2
    // std::erase(s, ' ');  // С++20

    // // В С++17 пришлось бы написать
    // // s.erase(std::remove(s.begin(), s.end(), ' '), s.end());

    // if (std::equal(s.begin(), s.begin() + s.size() / 2, s.rbegin())) {
    //     std::cout << "YES\n";
    // } else {
    //     std::cout << "NO\n";
    // }
}

