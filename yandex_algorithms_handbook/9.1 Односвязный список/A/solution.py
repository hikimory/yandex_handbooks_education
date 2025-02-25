class LinkedNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.length = 0

    def count(self):
        return self.length

    def init(self, val):
        self.head = LinkedNode(val)
        self.tail = self.head

    def add_last(self, val):
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next
        self.length += 1
    
    def add_first(self, val):
        self.head = LinkedNode(val, self.head)
        self.length += 1

    def get_node_by_index(self, index):
        temp = self.head
        idx = 1
        while idx < index:
            temp = temp.next
            idx += 1
        return temp

    def insert(self, index, value):
        if self.length == 0:
            self.init(value)
        else:
            match index:
                case 0:
                    self.add_first(value)
                case self.length:
                    self.add_last(value)
                case _:
                    temp = self.get_node_by_index(index)
                    temp.next = LinkedNode(value, temp.next)
        self.length += 1
    
    def remove(self, index):
        if index == 1:
            self.head = self.head.next
        else:
            temp = self.get_node_by_index(index - 1)
            temp.next = temp.next.next
        self.length -= 1

def main():
    link = LinkedList()
    answer = []
    n = int(input())
    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1], query[2]
            link.insert(x, y)
        elif query[0] == 2:
            answer.append(str(link.get_node_by_index(query[1]).value))
        elif query[0] == 3:
            link.remove(query[1])
    print('\n'.join(answer))


if __name__ == "__main__":
    main()