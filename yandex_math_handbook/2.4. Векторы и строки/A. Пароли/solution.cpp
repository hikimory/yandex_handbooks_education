#include <iostream>
#include <string>
#include <cctype> // Для std::isupper, std::islower, std::isdigit

bool IsGood(const std::string& password) {
    if (password.size() < 8 || password.size() > 14) {
        return false;
    }
    int upper = 0;
    int lower = 0;
    int digit = 0;
    int other = 0;

    for (char c : password) {
        if (c < 33 || c > 126) {
            return false;
        }
        if ('A' <= c && c <= 'Z') {
            upper = 1;
        } else if ('a' <= c && c <= 'z') {
            lower = 1;
        } else if ('0' <= c && c <= '9') {
            digit = 1;
        } else {
            other = 1;
        }
    }

    return upper + lower + digit + other >= 3;
}

bool IsGood(const std::string& password) {
    if (password.length() < 8 || password.length() > 14) {
        return false;
    }

    bool hasUpper = false;
    bool hasLower = false;
    bool hasDigit = false;
    bool hasOther = false;

    for (char c : password) {
        if (c < 33 || c > 126) {
            return false;
        }

        if (std::isupper(c)) {
            hasUpper = true;
        } else if (std::islower(c)) {
            hasLower = true;
        } else if (std::isdigit(c)) {
            hasDigit = true;
        } else {
            hasOther = true;
        }
    }

    int categoryCount = hasUpper + hasLower + hasDigit + hasOther;
    return categoryCount >= 3;
}

int main() {
    std::string password;
    std::getline(std::cin, password);
    if (IsGood(password)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
}