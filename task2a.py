class Stack:
    def __init__(self):
        self.items = []

    def push(self, building):
        if len(self.items) == 10:
            self.items.pop(0)
        self.items.append(building)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# Creating a stack
history = Stack()

# Adding buildings visited
history.push("Administration Block")
history.push("Library")
history.push("Computer Laboratory")
history.push("Main Hall")

print("Navigation History:", history.items)
print("Last building visited:", history.peek())
print("Removed building:", history.pop())
print("Is the stack empty?", history.is_empty())