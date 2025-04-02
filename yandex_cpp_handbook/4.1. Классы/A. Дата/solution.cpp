const int DEFAULT_DATE_DAY = 1;
const int DEFAULT_DATE_MONTH = 1;
const int DEFAULT_DATE_YEAR = 1970;
const int DAYS_IN_YEAR_WITHOUT_FEB = 337;

class Date {
    private:
        int d, m, y;
    
        int GetDaysInFeb(int year) const;
        int GetDaysInMonth(int month, int year) const;
        int GetDaysInYear(int year) const;
        bool IsCorrectDate() const;
        int DaysPassedToMonth(int month, int year) const;
        int GetDays() const;
        void SetFromDays(int days);
    
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

bool Date::IsCorrectDate() const {
    return GetMonth() <= 12 && GetMonth() >= 1 && GetDay() <= GetDaysInMonth(GetMonth(), GetYear()) && GetDay() > 0;
}

int Date::DaysPassedToMonth(int month, int year) const {
    int days = 0;
    for (int i = 1; i < month; ++i) {
        days += GetDaysInMonth(i, year);
    }
    return days;
}

int Date::GetDays() const {
    int days = 0;
    for (int i = DEFAULT_DATE_YEAR; i < GetYear(); ++i) {
        days += GetDaysInYear(i);
    }
    return days + DaysPassedToMonth(GetMonth(), GetYear()) + GetDay();
}

void Date::SetFromDays(int days) {
    d = DEFAULT_DATE_DAY;
    m = DEFAULT_DATE_MONTH;
    y = DEFAULT_DATE_YEAR;

    while (days > GetDaysInYear(GetYear())) {  // сначала определяем год
        days -= GetDaysInYear(GetYear());
        ++y;
    }

    while (days > DaysPassedToMonth(GetMonth() + 1, GetYear())) {  // определяем месяц
        ++m;
    }

    d = days - DaysPassedToMonth(GetMonth(), GetYear());  // остаток в дни
}

// Когда подготовительная часть закончена, реализуем публичный интерфейс:
Date::Date(int day, int month, int year)
        : d{day}, m{month}, y{year} {
    if (!IsCorrectDate()) {
        d = DEFAULT_DATE_DAY;
        m = DEFAULT_DATE_MONTH;
        y = DEFAULT_DATE_YEAR;
    }
}

int Date::GetDay() const {
    return d;
}

int Date::GetMonth() const {
    return m;
}

int Date::GetYear() const {
    return y;
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