class Stack:
    def __init__(self, size=15) -> None:
        self.size = size
        self.stack = [None]*self.size
        self.top = 0

    def is_empty(self):
        return not bool(self.top)

    def push(self, data):
        if self.top >= self.size-1:
            self.size += 5
            self.expand(self.size)
        self.stack[self.top] = data

    def pop(self):
        if not self.is_empty():
            self.contract()
            temp = self.stack[self.top]
            self.stack.pop()
            return temp
        else:
            print("The Stack is empty")

    def expand(self, expandSize: int):
        temp = self.stack
        self.stack = None*expandSize
        for i in range(len(temp)):
            self.stack[i] = temp[i]

    def contract(self):
        if self.top < ((self.size-1)//2) and self.size//2 > 15:
            self.size = (self.size*75)//100
            self.stack = self.stack[:self.size-1]

    def display(self):
        for i in self.stack:
            print(i)
