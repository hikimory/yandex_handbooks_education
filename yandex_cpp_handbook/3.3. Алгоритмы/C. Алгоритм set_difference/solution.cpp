// Объяснение:
// Итерация: Функция проходит по обоим диапазонам одновременно, используя итераторы first1 и first2.
// Сравнение элементов:
// Если элемент из первого диапазона меньше элемента из второго диапазона (*first1 < *first2), это означает, что этот элемент присутствует только в первом диапазоне. Мы копируем его в выходную последовательность (*out++ = *first1++).
// Если элемент из второго диапазона меньше элемента из первого диапазона (*first2 < *first1), это означает, что элемент из второго диапазона не присутствует в первом. Мы просто пропускаем его (++first2).
// Если элементы равны (*first1 == *first2), это означает, что они присутствуют в обоих диапазонах. Мы пропускаем оба элемента (++first1, ++first2).
// Копирование оставшихся элементов: После того как один из диапазонов закончился, мы копируем оставшиеся элементы из первого диапазона в выходную последовательность, используя std::copy.
// Возврат итератора: Функция возвращает итератор, указывающий на конец выходной последовательности.


template <typename InIter1, typename InIter2, typename OutIter>
OutIter SetDifference(InIter1 first1, InIter1 last1,
                      InIter2 first2, InIter2 last2,
                      OutIter out) {
    while (first1 != last1 && first2 != last2) {
        if (*first1 < *first2) {
            *out++ = *first1++;
        } else if (*first2 < *first1) {
            ++first2;
        } else { // *first1 == *first2
            ++first1;
            ++first2;
        }
    }
    return std::copy(first1, last1, out);
}