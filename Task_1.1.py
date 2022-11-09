
class Stack:
    def __init__(self, some_string):
        if isinstance(some_string, int):
            self.some_string = list(str(some_string))
        else:
            self.some_string = list(some_string)

    def return_reverse_string(self):
        new = ""
        new_lst = []
        for i in range(len(self.some_string)):
            new += self.some_string.pop()
        return new


a = Stack("12345")
b = Stack("Hello")
c = Stack(54321)

print(a.return_reverse_string())
print(b.return_reverse_string())
print(c.return_reverse_string())


