class Stack:
    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def is_empty(self):
        return False if self.array else True
    
    def back(self):
        if self.is_empty():
            return -1
        return self.array[-1]

def main():
    stack = Stack()
    n = int(input())
    queries = [int(x) for x in input().split()]
    answer = [0] * n
    for i in range(n):
        while stack.is_empty() == False and queries[i] > stack.back()[0]:
            elem, num = stack.pop()
            answer[i] += answer[num] + 1
        stack.push((queries[i], i))
    print(*answer)

if __name__ == "__main__":
    main()