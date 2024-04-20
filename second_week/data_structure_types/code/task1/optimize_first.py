from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        if len(self.queue1) == 1:   # Special case: last element
            return self.queue1.popleft()

        # Move all but the last element to queue2
        for _ in range(len(self.queue1) - 1):
            self.queue1.append(self.queue1.popleft())

        top_el = self.queue1.popleft()  # Retrieve the last element (top)
        return top_el

    def top(self) -> int:
        if not self.empty():
            for _ in range(len(self.queue1) - 1):
                self.queue1.append(self.queue1.popleft())
            top_el = self.queue1[0]  # Peek at the top
            self.queue1.append(self.queue1.popleft())  # Restore original state
            return top_el

    def empty(self) -> bool:
        return not self.queue1

class MyQueue:
    def __init__(self):
        self.in_stack = deque()  # For enqueueing
        self.out_stack = deque()  # For dequeueing

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move_in_to_out()  # Ensure dequeue elements are ready
        return self.out_stack.pop() 

    def peek(self) -> int:
        self._move_in_to_out()  
        return self.out_stack[-1] 

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move_in_to_out(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())