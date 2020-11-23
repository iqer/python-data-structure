class StackQueue:

    def __init__(self):
        self.stackA = list()
        self.stackB = list()

    def enqueue(self, element):
        self.stackA.append(element)
        pass

    def dequeue(self):
        if len(self.stackB) == 0:
            if len(self.stackA) == 0:
                raise Exception('队列以空!')
            self.transfer()
        return self.stackB.pop()

    def transfer(self):
        while len(self.stackA) > 0:
            self.stackB.append(self.stackA.pop())


if __name__ == '__main__':
    stack_queue = StackQueue()
    stack_queue.enqueue(1)
    stack_queue.enqueue(2)
    stack_queue.enqueue(3)
    print(stack_queue.dequeue())
    print(stack_queue.dequeue())
    stack_queue.enqueue(4)
    print(stack_queue.dequeue())
    print(stack_queue.dequeue())