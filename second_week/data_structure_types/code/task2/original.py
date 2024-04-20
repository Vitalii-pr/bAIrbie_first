from collections import deque

class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_el = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_el

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        top_el = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_el

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


class MyQueue:
    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        new_s = Stack()
        while not self.stack.empty():
            new_s.push(self.stack.pop())
        self.stack.push(x)
        while not new_s.empty():
            self.stack.push(new_s.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack.top()

    def empty(self) -> bool:
        return self.stack.empty()

class MyStack:

    def __init__(self):
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def push(self, x: int) -> None:
        self.queue2.push(x)
        while not self.queue1.empty():
            self.queue2.push(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.empty()