#include <tuple>

const int DEFAULT_DATE_DAY = 1;
const int DEFAULT_DATE_MONTH = 1;
const int DEFAULT_DATE_YEAR = 1970;
const int DAYS_IN_YEAR_WITHOUT_FEB = 337;

class Date {
private:
    int days{0};

    int GetDaysInFeb(int year) const;
    int GetDaysInMonth(int month, int year) const;
    int GetDaysInYear(int year) const;
    int DaysPassedToMonth(int month, int year) const;

    void SetDays(int day, int month, int year);
    std::tuple<int, int, int> ToDate() const;
    void SetFromDays(int inp_days);
    int GetDays() const;

public:
    Date(int day, int month, int year);

    int GetDay() const;
    int GetMonth() const;
    int GetYear() const;

    Date operator+(int k) const;
    Date operator-(int k) const;
    int operator-(const Date& other) const;
};

int Date::GetDaysInFeb(int year) const {
    if ((!(year % 4) && (year % 100)) || !(year % 400)) {
        return 29;
    }
    return 28;
}

int Date::GetDaysInMonth(int month, int year) const {
    switch (month) {
        case 2:
            return GetDaysInFeb(year);
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            return 31;
        default:
            return 30;
    }
}

int Date::GetDaysInYear(int year) const {
    return DAYS_IN_YEAR_WITHOUT_FEB + GetDaysInFeb(year);
}

int Date::DaysPassedToMonth(int month, int year) const {
    int result = 0;
    for (int i = 1; i < month; ++i) {
        result += GetDaysInMonth(i, year);
    }
    return result;
}

void Date::SetDays(int day, int month, int year) {
    days = 0;
    for (int i = DEFAULT_DATE_YEAR; i < year; ++i) {
        days += GetDaysInYear(i);
    }
    days = days + DaysPassedToMonth(month, year) + day;
}

std::tuple<int, int, int> Date::ToDate() const {
    int inp_days = days;
    int month = DEFAULT_DATE_MONTH;
    int year = DEFAULT_DATE_YEAR;

    while (inp_days > GetDaysInYear(year)) {  // сначала определяем год
        inp_days -= GetDaysInYear(year);
        ++year;
    }

    while (inp_days > DaysPassedToMonth(month + 1, year)) {  // определяем месяц
        ++month;
    }

    int day = inp_days - DaysPassedToMonth(month, year);  // остаток в дни
    return {day, month, year};
}

void Date::SetFromDays(int inp_days) {
    days = inp_days;
}

int Date::GetDays() const {
    return days;
}

Date::Date(int day, int month, int year) {
    if (month > 12 || month < 1 || day > GetDaysInMonth(month, year) || day < 1) {
        days = 0;
    } else {
        SetDays(day, month, year);
    }
}

int Date::GetDay() const {
    return std::get<0>(ToDate());
}

int Date::GetMonth() const {
    return std::get<1>(ToDate());
}

int Date::GetYear() const {
    return std::get<2>(ToDate());
}

Date Date::operator+(int k) const {
    Date result(*this);
    result.SetFromDays(result.GetDays() + k);
    return result;
}

Date Date::operator-(int k) const {
    Date result(*this);
    result.SetFromDays(result.GetDays() - k);
    return result;
}

int Date::operator-(const Date& other) const {
    return GetDays() - other.GetDays();
}