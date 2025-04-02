#include <set>
#include <vector>
#include <cstdint>

class Stock {
private:
    struct WeightNumber {
        int w;
        size_t i;

        bool operator < (const WeightNumber& other) const {
            if (w == other.w) {
                return i > other.i;
            }
            return w < other.w;
        }
    };

    struct VolumeNumber {
        int v;
        size_t i;

        bool operator < (const VolumeNumber& other) const {
            if (v == other.v) {
                return i > other.i;
            }
            return v < other.v;
        }
    };

    struct Iterators {
        std::set<WeightNumber>::iterator byW;
        std::set<VolumeNumber>::iterator byV;
    };

    std::vector<Iterators> boxes;
    std::set<WeightNumber> sortedByW;
    std::set<VolumeNumber> sortedByV;

public:
    void Add(int w, int v) {
        size_t num = boxes.size();
        boxes.push_back({sortedByW.insert({w, num}).first, sortedByV.insert({v, num}).first});
    }

    int GetByW(int min_w) {
        const auto it = sortedByW.lower_bound({min_w, boxes.size()});
        if (it == sortedByW.end()) {
            return -1;
        }

        size_t res = it->i;
        sortedByW.erase(it);
        sortedByV.erase(boxes[res].byV);
        return res;
    }

    int GetByV(int min_v) {
        const auto it = sortedByV.lower_bound({min_v, boxes.size()});
        if (it == sortedByV.end()) {
            return -1;
        }

        size_t res = it->i;
        sortedByV.erase(it);
        sortedByW.erase(boxes[res].byW);
        return res;
    }
};