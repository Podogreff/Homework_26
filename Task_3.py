class Stack:
    def __init__(self):
        self.values = []

    def add(self, item):
        self.values.append(item)
        print(f"You just added '{item}' to the stack")

    def get_from_stack(self, name):
        if name in self.values:
            return f"Index of the '{name}' element in the stack is: {self.values.index(name)}"
        else:
            raise ValueError("There is no such element in the stack")

    def pop_item(self):
        return self.values.pop()

    def print_full_stack(self):
        if self.values:
            return f"Here is the full stack: {self.values}"
        raise ValueError("The Stack is empty")


stack = Stack()

stack.add("Vlad")
stack.add("Khimich")
stack.add("Oleksandrovych")
print(stack.print_full_stack())
print(stack.get_from_stack("Vlad"))
print(stack.get_from_stack("12"))
print(stack.print_full_stack())


