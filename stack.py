class Stack:
    def __init__(self):
        self._items = []
    def is_empty(self):
        return not bool(self._items)
    def push(self, item):
        return self._items.append(item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def size(self):
        return len(self._items)
    

s = Stack()
print(s.is_empty())

s.push(4)

print(s.peek())

s.push(4)
s.push(5)
s.push(6)
s.push("True")

print(s.pop())
print(s.peek())
print(s.size())