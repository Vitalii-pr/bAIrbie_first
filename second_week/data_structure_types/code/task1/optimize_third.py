class MyQueue:
    def __init__(self):
        self.input_stack = []  # Maintains order of incoming elements
        self.output_stack = []  # Reordered for popping

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move_elements()  # Transfer if the output stack is empty
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move_elements()  # Transfer if the output stack is empty
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def _move_elements(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())