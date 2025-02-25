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
    arr = Stack()
    n = int(input())
    answer = []
    for _ in range(n):
        query = input().split()
        if query[0] == '1':
            arr.push(query[1])
        elif query[0] == '2':
            arr.pop()   
        answer.append(str(arr.back()))
    print('\n'.join(answer))

if __name__ == "__main__":
    main()