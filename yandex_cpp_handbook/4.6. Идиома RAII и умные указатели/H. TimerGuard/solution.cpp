#include <iostream>
#include <chrono>
#include <string>

class TimerGuard {
    std::chrono::time_point<std::chrono::high_resolution_clock> start;
    std::string outMessage;
    std::ostream& outStream;
public:

    TimerGuard(std::string message = "", std::ostream& out = std::cout):
        start(std::chrono::high_resolution_clock::now()),  // start - вызов конструктора
        outMessage(message),
        outStream(out)
    {}

    ~TimerGuard() {
        auto end = std::chrono::high_resolution_clock::now();  // конец - вызов деструктора
        std::chrono::duration<double> diff = end - start;
        outStream << outMessage << " " << diff.count() << "\n";
    }
};