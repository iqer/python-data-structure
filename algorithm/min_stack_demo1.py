class MinStack:

    def __init__(self):
        self.main_stack = list()
        self.min_stack = list()

    def push(self, data):
        self.main_stack.append(data)
        if len(self.min_stack) == 0 or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        pop_data = self.main_stack.pop()
        if pop_data == self.min_stack[-1]:
            self.min_stack.pop()
        return pop_data

    def get_min(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


if __name__ == '__main__':
    my_stack = MinStack()
    my_stack.push(4)
    my_stack.push(9)
    my_stack.push(7)
    my_stack.push(3)
    my_stack.push(8)
    my_stack.push(5)
    print(my_stack.get_min())
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(my_stack.get_min())
