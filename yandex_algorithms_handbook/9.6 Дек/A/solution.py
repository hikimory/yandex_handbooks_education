class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addBack(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        if self.size == 0:
            return -1
        return self.items.pop()

    def removeBack(self):
        if self.size == 0:
            return -1
        return self.items.pop(0)

    def getFront(self):
        if self.size == 0:
            return -1
        return self.items[-1]

    def getBack(self):
        if self.size == 0:
            return -1
        return self.items[0]

    def size(self):
        return len(self.items)

def main():
    deq = Deque()
    n = int(input())
    answer = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            deq.addFront(query[1])
        elif query[0] == '2':
            deq.removeBack()
        t = '-1'
        if deq.size() > 0:
            t = deq.getBack()
        answer.append(t)
    print('\n'.join(answer))

if __name__ == "__main__":
    main()
