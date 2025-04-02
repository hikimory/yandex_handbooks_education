#include <vector>

std::vector<std::vector<int>> Transpose(const std::vector<std::vector<int>>& matrix) {
    const size_t m = matrix.size();
    const size_t n = matrix[0].size();

    std::vector<std::vector<int>> result(n);
    for (size_t j = 0; j != n; ++j) {
        result[j].resize(m);
        for (size_t i = 0; i != m; ++i) {
            result[j][i] = matrix[i][j];
        }
    }
    return result;
}