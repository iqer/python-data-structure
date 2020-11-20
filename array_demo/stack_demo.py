from list_demo import LinkedList


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.link_list = LinkedList()
        self.bottom = None
        self.top = None

    def push(self, data):
        self.link_list.insert(self.link_list.size, data)
        if self.link_list.size == 0:
            self.bottom = self.top = data
        else:
            self.top = data

    def pop(self):
        pop_node = self.link_list.get(self.link_list.size-1)
        prev_node = self.link_list.get(self.link_list.size-2)
        self.link_list.remove(self.link_list.size-1)
        self.top = prev_node.data
        return pop_node

    def output(self):
        self.link_list.output()


if __name__ == '__main__':
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.pop()
    s1.output()
