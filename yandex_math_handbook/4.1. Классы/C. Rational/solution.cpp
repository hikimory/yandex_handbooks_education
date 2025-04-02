#include <numeric>

class Rational {
private:
    int num;
    int denom;

    void Reduce() {
        int d = std::gcd(num, denom);
        num /= d;
        denom /= d;
        if (denom < 0) {
            num *= -1;
            denom *= -1;
        }
    }

public:
    Rational(int num_ = 0, int denom_ = 1) : num(num_), denom(denom_) {
        Reduce();
    }

    int Numerator() const {
        return num;
    }

    int Denominator() const {
        return denom;
    }

    // унарный плюс (формально ничего не меняет)
    Rational operator + () const {
        return {num, denom};
    }

    // унарный минус
    Rational operator - () const {
        return Rational(-num, denom);
    }

    // rhs - сокращение от right hand side (правый аргумент бинарного оператора)
    Rational& operator += (const Rational& rhs) {
        num = num * rhs.denom + rhs.num * denom;
        denom *= rhs.denom;
        Reduce();
        return *this;
    }

    Rational& operator -= (const Rational& rhs) {
        num = num * rhs.denom - rhs.num * denom;
        denom *= rhs.denom;
        Reduce();
        return *this;
    }

    Rational& operator *= (const Rational& rhs) {
        num *= rhs.num;
        denom *= rhs.denom;
        Reduce();
        return *this;
    }

    Rational& operator /= (const Rational& rhs) {
        // сохраняем старый числитель, чтобы корректно работало выражение q /= q.
        int tmp = rhs.num;
        num *= rhs.denom;
        denom *= tmp;
        Reduce();
        return *this;
    }
};

Rational operator + (const Rational& lhs, const Rational& rhs) {
    Rational result = lhs;
    result += rhs;
    return result;
}

Rational operator - (const Rational& lhs, const Rational& rhs) {
    Rational result = lhs;
    result -= rhs;
    return result;
}

Rational operator * (const Rational& lhs, const Rational& rhs) {
    Rational result = lhs;
    result *= rhs;
    return result;
}

Rational operator / (const Rational& lhs, const Rational& rhs) {
    Rational result = lhs;
    result /= rhs;
    return result;
}

bool operator == (const Rational& lhs, const Rational& rhs) {
    return lhs.Numerator() == rhs.Numerator() && lhs.Denominator() == rhs.Denominator();
}

bool operator != (const Rational& lhs, const Rational& rhs) {
    return !(lhs == rhs);
}