#include <iostream>
#include <memory>
#include <string>

class Expression {
public:
    virtual int Evaluate() const = 0;
    virtual std::string ToString() const = 0;
    virtual ~Expression() {}
};

using ExpressionPtr = std::shared_ptr<Expression>;

class ConstExpr : public Expression {
private:
    int value;

public:
    ConstExpr(int v) : value(v) {}

    int Evaluate() const override {
        return value;
    }
    std::string ToString() const override {
        return std::to_string(value);
    }
};

class BinaryOperation : public Expression {
protected:
    ExpressionPtr left;
    ExpressionPtr right;

public:
    BinaryOperation(ExpressionPtr l, ExpressionPtr r) : left(l), right(r) {}
};

class SumExpr : public BinaryOperation {
public:
    SumExpr(ExpressionPtr l, ExpressionPtr r) : BinaryOperation(l, r) {}

    int Evaluate() const override {
        return left->Evaluate() + right->Evaluate();
    }

    std::string ToString() const override {
        return left->ToString() + " + " + right->ToString();
    }
};

class ProductExpr : public BinaryOperation {
private:
    static std::string Parentheses(ExpressionPtr ex) {
        if (dynamic_cast<SumExpr*>(ex.get())) {
            return std::string("(") + ex->ToString() + ")";
        }
        else {
            return ex->ToString();
        }
    }
public:
    ProductExpr(ExpressionPtr l, ExpressionPtr r) : BinaryOperation(l, r) {}

    int Evaluate() const override {
        return left->Evaluate() * right->Evaluate();
    }

    std::string ToString() const override {
        return Parentheses(left) + " * " + Parentheses(right);
    }
};

ExpressionPtr Const(int x) {
    return std::make_shared<ConstExpr>(x);
}

ExpressionPtr Sum(ExpressionPtr l, ExpressionPtr r) {
    return std::make_shared<SumExpr>(l, r);
}

ExpressionPtr Product(ExpressionPtr l, ExpressionPtr r) {
    return std::make_shared<ProductExpr>(l, r);
}