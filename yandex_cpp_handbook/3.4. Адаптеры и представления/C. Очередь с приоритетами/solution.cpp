#include <iostream>
#include <queue>

int main() {
    std::priority_queue<int> pq;

    std::string command;
    while (std::cin >> command) {
        if (command == "CLEAR") {
            while (!pq.empty()) {
                pq.pop();
            }
        } else if (command == "ADD") {
            int x;
            std::cin >> x;
            pq.push(x);
        } else if (command == "EXTRACT") {
            if (pq.empty()) {
                std::cout << "CANNOT\n";
            } else {
                std::cout << pq.top() << "\n";
                pq.pop();
            }
        }
    }
}