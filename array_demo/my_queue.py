class MyQueue:
    def __init__(self, capacity):
        self.content_list = [None] * capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, data):
        if (self.rear + 1) % len(self.content_list) == self.front:
            raise Exception('队列已满')
        self.content_list[self.rear] = data
        self.rear = (self.rear + 1) % len(self.content_list)

    def dequeue(self):
        if self.front == self.rear:
            raise Exception('队列已空')
        dequeue_data = self.content_list[self.front]
        self.front = (self.front + 1) % len(self.content_list)
        return dequeue_data

    def output(self):
        i = self.front
        while i != self.rear:
            print(self.content_list[i])
            i = (i + 1) % len(self.content_list)


if __name__ == '__main__':
    my_queue = MyQueue(10)
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
