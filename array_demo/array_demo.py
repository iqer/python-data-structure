myList = [1, 2, 3, 4, 5, 6]

myList.append(7)
#
# print(myList)
#
#
# myList.insert(3, 8)
#
# print(myList)


class MyList(object):

    def __init__(self, capacity):
        self.size = 0
        self.array = [None] * capacity

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError('索引值异常')
        if self.size >= len(self.array):
            self.resize()
        for i in range(self.size-1, index-1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def resize(self):
        new_array = [None] * self.size * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('索引值异常!')
        for i in range(index, self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1


if __name__ == '__main__':
    ml = MyList(5)
    # ml.insert(0, 1)
    # ml.insert(1, 2)
    # ml.insert(2, 3)
    # ml.insert(1, 4)
    ml.insert(0, 10)
    ml.insert(0, 11)
    ml.insert(0, 12)
    ml.insert(0, 13)
    ml.insert(0, 14)
    ml.insert(0, 15)
    ml.remove(0)
    ml.output()
