from collections import deque

class Stack:
    def __init__(self):
        self._data = deque()  # Single underlying deque 

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        return self._data.pop()

    def top(self) -> int:
        return self._data[-1] 

    def empty(self) -> bool:
        return not self._data


class MyQueue:
    def __init__(self):
        self._data = deque()  # Single underlying deque

    def push(self, x: int) -> None:
        self._data.append(x)

    def pop(self) -> int:
        return self._data.popleft()

    def peek(self) -> int:
        return self._data[0]

    def empty(self) -> bool:
        return not self._data


class MyStack:
    """Efficient stack implementation using a single queue."""
    def __init__(self):
        self._queue = deque()  

    def push(self, x: int) -> None:
        self._queue.append(x)
        # Rotate elements to keep the newest at the front
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()  

    def top(self) -> int:
        return self._queue[0] 

    def empty(self) -> bool:
        return not self._queue