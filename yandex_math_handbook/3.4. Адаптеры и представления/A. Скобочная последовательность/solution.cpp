#include <iostream>
#include <stack>
#include <string>
#include <map>

bool IsCorrect(const std::string& sequence) {
    std::stack<char> brackets;
    std::map<char, char> matchingBrackets = {
        {'(', ')'},
        {'{', '}'},
        {'[', ']'}
    };

    for (char bracket : sequence) {
        if (matchingBrackets.count(bracket)) {
            brackets.push(bracket);
        } else {
            if (brackets.empty()) {
                return false;
            }

            char top = brackets.top();
            
            if (matchingBrackets[top] == bracket) {
                brackets.pop();
            } else {
                return false;
            }
        }
    }

    return brackets.empty();
}

int main() {
    std::string sequence;
    std::getline(std::cin, sequence);
    if (IsCorrect(sequence)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
    return 0;
}