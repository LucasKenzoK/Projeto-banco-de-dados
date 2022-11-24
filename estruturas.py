class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len (self.items) -1]

class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def add(self,item):
        self.items.insert(0,item)
    def remove(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

