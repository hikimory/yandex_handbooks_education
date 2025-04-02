# Tree-2
<table>
 <tr>
    <td>Ограничение времени</td>
    <td>2 c</td>
 </tr>
 <tr>
    <td>Ограничение памяти</td>
    <td>64 Mb</td>
 </tr>
  <tr>
    <td>Ввод</td>
    <td>стандартный ввод или input.txt</td>
 </tr>
  <tr>
    <td>Вывод</td>
    <td>стандартный ввод или input.txt</td>
 </tr>
</table>

Коля пишет класс «Дерево». Узел дерева может хранить целое число, а также знает о своём родителе и о своих потомках. У узла есть функция AddChild для добавления потомка с заданным числовым значением, а также функция Print для красивой печати поддерева начиная с этого узла.

Вот что получилось у Коли:

```cpp
#include <iostream>
#include <vector>

class TreeNode {
private:
    int value;
    TreeNode* root = nullptr;
    std::vector<TreeNode*> children;

public:
    TreeNode(int val): value(val) {
    }

    TreeNode(const TreeNode&) = delete;
    TreeNode& operator=(const TreeNode&) = delete;

    TreeNode* AddChild(int child_value) {
        auto node = new TreeNode(child_value);
        node->root = this;
        children.push_back(node);
        return node;
    }

    void Print(int depth = 0) const {
        for (int i = 0; i < depth; ++i) {
            std::cout << " ";
        }
        std::cout << "- " << value << "\n";
        for (const auto& child : children) {
            child->Print(depth + 1);
        }
    }
};
```

Использоваться этот класс будет примерно так:

```cpp
#include "tree.h"

int main() {
    TreeNode root(1);

    auto left_son = root.AddChild(10);
    auto middle_son = root.AddChild(20);
    auto right_son = root.AddChild(30);

    left_son->AddChild(100);
    left_son->AddChild(200);

    root.Print();
}
```

Однако эта работающая на первый взгляд тестовая программа падает, если её собрать с адресным санитайзером. Исправьте код класса TreeNode, чтобы решить эту проблему.

## Примечание
Сдайте в систему только код класса TreeNode без функции main. Подключите все необходимые для вашей реализации библиотеки.