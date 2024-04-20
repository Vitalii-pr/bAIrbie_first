class MyStack:
    def __init__(self):
        self.stack = []  # Use a single list for the stack
        self.active = 0  # Pointer to the active part of the list

    def push(self, x: int) -> None:
        self.stack.append(x)  # Append directly to the list
        self.active += 1  # Increment the active pointer

    def pop(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty")  # Handle empty stack
        self.active -= 1  # Decrement the active pointer
        return self.stack.pop(self.active)  # Pop from the active part

    def top(self) -> int:
        if self.empty():
            raise ValueError("Stack is empty")  # Handle empty stack
        return self.stack[self.active - 1]  # Access the top element

    def empty(self) -> bool:
        return self.active == 0