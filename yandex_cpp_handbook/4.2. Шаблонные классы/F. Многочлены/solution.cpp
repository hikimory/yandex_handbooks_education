#include <algorithm>
#include <iostream>
#include <vector>

template <typename T>
class Polynomial {
public:
    using Container = typename std::vector<T>;
    using ConstIterator = typename Container::const_iterator;

private:
    Container coefficients;
    inline static const T valueTypeZero{0};

    void Normalize() {
        while (!coefficients.empty() && coefficients.back() == valueTypeZero) {
            coefficients.pop_back();
        }
    }

    Container& GetCoefficients() {
        return coefficients;
    }

public:
    Polynomial(const Container& coeffs)
        : coefficients{coeffs} {
            Normalize();
        }

    Polynomial(const T& value = {}) {
        if (value != valueTypeZero) {
            coefficients.push_back(value);
        }
    }

    template<typename ForwardIt>
    Polynomial(ForwardIt first, ForwardIt last)
        : coefficients{first, last} {
            Normalize();
    }

    const Container& GetCoefficients() const {
        return coefficients;
    }

    friend bool operator == (const Polynomial<T>& lhs, const Polynomial<T>& rhs) {
        return lhs.GetCoefficients() == rhs.GetCoefficients();
    }

    friend bool operator != (const Polynomial<T>& lhs, const Polynomial<T>& rhs) {
        return !(lhs == rhs);
    }

    Polynomial<T>& operator += (const Polynomial<T>& other) {
        if (other.Degree() > Degree()) {
            GetCoefficients().resize(other.Degree() + 1);
        }

        for (int i = 0; i <= Degree() && i <= other.Degree(); ++i) {
            GetCoefficients()[i] += other.GetCoefficients()[i];
        }
        Normalize();
        return *this;
    }

    Polynomial<T>& operator -= (const Polynomial<T>& other) {
        if (other.Degree() > Degree()) {
            GetCoefficients().resize(other.Degree() + 1);
        }

        for (int i = 0; i <= Degree() && i <= other.Degree(); ++i) {
            GetCoefficients()[i] -= other.GetCoefficients()[i];
        }
        Normalize();
        return *this;
    }

    Polynomial<T>& operator *= (const Polynomial<T>& other) {
        if (Degree() == -1 || other.Degree() == -1) {
            GetCoefficients().resize(0);
            return *this;
        }

        std::vector<T> tmp(Degree() + other.Degree() + 1);
        for (int i = 0; i <= Degree(); ++i) {
            for (int j = 0; j <= other.Degree(); ++j) {
                tmp[i + j] += GetCoefficients()[i] * other.GetCoefficients()[j];
            }
        }
        GetCoefficients() = std::move(tmp);
        Normalize();
        return *this;
    }

    friend Polynomial<T> operator + (Polynomial<T> lhs, const Polynomial<T>& rhs) {
        return lhs += rhs;
    }

    friend Polynomial<T> operator - (Polynomial<T> lhs, const Polynomial<T>& rhs) {
        return lhs -= rhs;
    }

    friend Polynomial<T> operator * (Polynomial<T> lhs, const Polynomial<T>& rhs) {
        return lhs *= rhs;
    }

    int Degree() const {
        return static_cast<int>(GetCoefficients().size()) - 1;
    }

    const T& operator [] (size_t power) const {
        if (static_cast<int>(power) > Degree()) {
            return valueTypeZero;
        }
        return GetCoefficients()[power];
    }

    T operator () (const T& given_value) const {
        T result = valueTypeZero;

        for (auto i = Degree(); i >= 0; --i) {
            result *= given_value;
            result += GetCoefficients()[i];
        }

        return result;
    }

    ConstIterator begin() const {
        return GetCoefficients().cbegin();
    }

    ConstIterator end() const {
        return GetCoefficients().cend();
    }
};

template<typename T>
std::ostream& operator<<(std::ostream& out, const Polynomial<T>& polynomial) {
    for (auto i = polynomial.Degree(); i >= 0; --i) {
        out << polynomial[i];
        if (i != 0) {
            out << ' ';
        }
    }
    return out;
}