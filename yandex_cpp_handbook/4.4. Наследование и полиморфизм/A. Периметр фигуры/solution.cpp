class Figure {
public:
    virtual int Perimeter() const = 0;
    virtual ~Figure() {}
};

class Rectangle : public Figure {
public:
    Rectangle(int w, int h) : width(w), height(h){}
    int Perimeter() const override {
        return 2 * (width + height);
    }
    ~Rectangle() {}

private:
    int width;
    int height;
};

class Triangle : public Figure {
public:
    Triangle(int f, int s, int t) : first(f), second(s), third(t){}
    int Perimeter() const override {
        return first + second + third;
    }
    ~Triangle() {}

private:
    int first;
    int second;
    int third;
};