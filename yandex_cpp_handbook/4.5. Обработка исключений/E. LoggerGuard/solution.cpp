#include <iostream>
#include <string>

class LoggerGuard {
private:
    std::string Message;
    std::ostream& Out;
public:
    LoggerGuard(const std::string& message, std::ostream& out = std::cout):
        Message(message), Out(out){}

    ~LoggerGuard() {
        Out << Message << "\n";
    }
};

// version 2

class LoggerGuard {
private:
    std::string Message;
    std::ostream* Out;
public:
    LoggerGuard(const std::string& message, std::ostream& out = std::cout) {
        Message = message;
        Out = &out;
    }

    ~LoggerGuard() {
        *Out << Message << "\n";
    }
};