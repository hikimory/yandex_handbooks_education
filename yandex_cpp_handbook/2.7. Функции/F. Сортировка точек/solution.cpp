#include <algorithm>
#include <iostream>
#include <vector>

struct Point {
    int x;
    int y;
    int distance;
};

int main() {
    size_t n;
    std::cin >> n;

    std::vector<Point> points(n);

    for (size_t i = 0; i != n; ++i) {
        std::cin >> points[i].x >> points[i].y;
        points[i].distance = points[i].x * points[i].x + points[i].y * points[i].y;
    }

    std::sort(
        points.begin(),
        points.end(),
        [](const Point& p1, const Point& p2) {
            return p1.distance < p2.distance;
        }
    );

    for (const auto& point : points) {
        std::cout << point.x << " " << point.y << "\n";
    }
}