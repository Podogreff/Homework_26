
class Stack:
    def __init__(self):
        self.stack = st

    def print_reverse_text(self):
        string = ""
        for elem in range(len(self.stack)):
            string += self.stack.pop()
        return string


if __name__ == "__main__":
    st = []
    num_of_symbols = int(input("Please enter the number of symbols u wanna enter: "))
    for i in range(1, num_of_symbols + 1):
        symbol = (input(f"Write {i} symbol: "))
        if isinstance(symbol, str):
            st.append(symbol)
        else:
            st.append(str(symbol))

    a = Stack()
    print(f"Here is your reverse string: {a.print_reverse_text()}")
