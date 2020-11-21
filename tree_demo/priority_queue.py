class PriorityQueue(object):

    def __init__(self):
        self.array = list()
        self.size = 0

    def enqueue(self, element):
        self.array.append(element)
        self.size += 1
        self.up_adjust()

    def dequeue(self):
        if self.size < 0:
            raise Exception('队列已空')
        head = self.array[0]
        self.array[0] = self.array[self.size-1]
        self.size -= 1
        self.down_adjust()
        return head

    def up_adjust(self):
        child_index = self.size - 1
        parent_index = (child_index - 1) // 2
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1) // 2
        self.array[child_index] = temp

    def down_adjust(self):
        parent_index = 0
        child_index = 1
        temp = self.array[parent_index]
        while child_index < self.size:
            if child_index + 1 < self.size and self.array[child_index] < self.array[child_index+1]:
                child_index += 1
            if temp >= self.array[child_index]:
                break
            self.array[parent_index] = self.array[child_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        self.array[parent_index] = temp


if __name__ == '__main__':
    deque = PriorityQueue()
    deque.enqueue(3)
    deque.enqueue(5)
    deque.enqueue(10)
    deque.enqueue(2)
    deque.enqueue(7)
    print(deque.dequeue())
    print(deque.dequeue())
