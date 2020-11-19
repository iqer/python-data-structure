class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('索引值异常!')
        p = self.head
        for i in range(index):
            p = p.next
        return p

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("索引值异常!")
        node = Node(data)

        if self.size == 0:
            self.head = None
            self.last = None

        # 头部插入
        elif index == 0:
            node.next = self.head
            self.head = node
        # 尾部插入
        elif index == self.size:
            self.last.next = node
            self.last = node
        # 中间插入
        else:
            prev_node = self.get(index-1)
            node.next = prev_node.next
            prev_node.next = node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('索引值异常!')
        # 删除头节点:
        if index == 0:
            removed_node = self.head
            self.head = self.head.next
        # 删除尾节点
        elif index == self.size - 1:
            prev_node = self.get(index-1)
            removed_node = prev_node.next
            self.last = prev_node
        # 删除中间节点
        else:
            prev_node = self.get(index-1)
            removed_node = prev_node.next
            prev_node.next = prev_node.next.next

        return removed_node

    def output(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next
