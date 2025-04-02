#include <iostream>
#include <string>

class NotifierBase {
public:
    virtual void Notify(const std::string& message) const = 0;
    virtual ~NotifierBase() {}
};

class SmsNotifier : public NotifierBase {
public:
    SmsNotifier(std::string&& number) // Конструктор перемещения
        : Number(std::move(number)) {}

    SmsNotifier(const std::string& number) // Конструктор копирования
        : Number(number) {}

    virtual void Notify(const std::string& message) const override {
        SendSms(Number, message);
    }

private:
    const std::string Number;
};
    
class EmailNotifier : public NotifierBase {
public:
    EmailNotifier(std::string&& email) // Конструктор перемещения
        : Email(std::move(email)) {}

    EmailNotifier(const std::string& email) // Конструктор копирования
        : Email(email) {}

    virtual void Notify(const std::string& message) const override {
        SendEmail(Email, message);
    }

private:
    const std::string Email;
};