class Queue:
    def __init__(self):
        self.values = []

    def add(self, item):
        self.values.append(item)
        print(f"You just added '{item}' to the queue")

    def get_from_stack(self, name):
        if name in self.values:
            return f"Index of the '{name}' element in the queue is: {self.values.index(name)}"
        else:
            raise ValueError("There is no such element in the queue")

    def pop_item(self):
        return f"You just poped the 1st element '{self.values.pop(0)}' from the queue"

    def print_full_stack(self):
        if self.values:
            return f"Here is the full queue: {self.values}"
        raise ValueError("The queue is empty")


queue = Queue()

queue.add("Vlad")
queue.add("Khimich")
queue.add("Oleksandrovych")
print(queue.print_full_stack())
print(queue.get_from_stack("Vlad"))
print(queue.pop_item())
print(queue.print_full_stack())


