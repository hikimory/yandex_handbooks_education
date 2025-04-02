#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> lines;

    std::string line;
    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    //Method 1: Print in reverse order
    std::vector<std::string> lines1 = lines;
    std::sort(lines1.begin(), lines1.end());
    for (int i = lines1.size() - 1; i >= 0; --i) {
        std::cout << lines1[i] << std::endl;
    }

    // Method 2: Use reverse iterators
    std::vector<std::string> lines2 = lines;
    std::sort(lines2.rbegin(), lines2.rend());
    for (size_t i = 0; i != lines2.size(); ++i) {
        std::cout << lines2[i] << "\n";
    }

    // Method 3: Use a custom comparison function
    std::vector<std::string> lines3 = lines;
    std::sort(lines3.begin(), lines3.end(), [](const std::string& a, const std::string& b) {
        return a > b; // Сортировка по убыванию
    });
    for (const auto& str : lines3) {
        std::cout << str << std::endl;
    }

    // Method 4: Use std::greater
    std::vector<std::string> lines4 = lines;
    std::sort(lines4.begin(), lines4.end(), std::greater<std::string>()); // Сортировка по убыванию
    for (const auto& str : lines4) {
        std::cout << str << std::endl;
    }

    return 0;
}