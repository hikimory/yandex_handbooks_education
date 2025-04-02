#include <iostream>
#include <string>

class Serializer {
public:
    virtual void BeginArray() = 0;
    virtual void AddArrayItem(const std::string& s) = 0;
    virtual void EndArray() = 0;
    virtual ~Serializer() {}
};

class JsonSerializer : public Serializer {
public:
    void BeginArray() override {
        if (!isFirst) {
            std::cout << ",[";
        }
        else {
            std::cout << "[";
        }

        isFirst = true;
    }

    void AddArrayItem(const std::string& str) override {
        if (!isFirst) {
            std::cout << ",";
        }
        std::cout << "\"" << str << "\"";
        isFirst = false;
    }

    void EndArray() override {
        std::cout << "]";
        isFirst = false;
    }

private:
    bool isFirst = true;
};