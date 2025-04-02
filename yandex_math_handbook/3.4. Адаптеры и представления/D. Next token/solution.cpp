#include <string_view>

bool NextToken(std::string_view& sv, char delim, std::string_view& tok) {
    if (sv.empty()) {
        return false;
    }

    auto pos = sv.find(delim);
    if (pos != sv.npos) {  // разделитель найден
        tok = sv.substr(0, pos);  // вырезаем очередной токен
        sv.remove_prefix(pos + 1);  // сдвигаем sv за разделитель
    } else {
        tok = sv;
        sv.remove_prefix(sv.size());  // формально тут получится пустая строка
    }
    return true;
}