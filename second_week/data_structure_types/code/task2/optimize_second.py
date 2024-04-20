from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        self.queue2.append(x)  # Push to the non-empty queue
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty")  # Handle empty stack case
        return self.queue1.popleft()

    def top(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty")  # Handle empty stack case
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1 