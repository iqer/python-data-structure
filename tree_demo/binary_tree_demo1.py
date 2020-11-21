class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_binary_tree(input_list=None):
    """
    构建二叉树
    :param input_list:
    :return:
    """
    if input_list is None or len(input_list) == 0:
        return None
    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node


def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node


def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node


def post_order_traversal(node):
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node


def pre_order_traversal_with_stack(node):
    """
    使用栈完成前序遍历
    :param node:
    :return:
    """
    # stack = list()
    # while node is not None or len(stack) > 0:
    #     while node is not None:
    #         print(node.data)
    #         stack.append(node)
    #         node = node.left
    #     if len(stack) > 0:
    #         node = stack.pop()
    #         node = node.right

    res = list()

    if node is None:
        return res

    stack = list()
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        res.append(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    print(res)


def in_order_traversal_with_stack(node):
    """
    使用栈完成中序遍历
    :param node:
    :return:
    """
    # stack = list()
    # while node is not None or len(stack) > 0:
    #     while node is not None:
    #         stack.append(node)
    #         node = node.left
    #     if len(stack) > 0:
    #         node = stack.pop()
    #         print(node.data)
    #         node = node.right

    res = list()
    if node is None:
        return res

    stack = list()

    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node.data)
            node = node.right
    print(res)


def post_order_traversal_with_satck(node):
    """
    使用栈完成后序遍历
    一个列表存遍历对象
    一个列表保存结果
    :param node:
    :return:
    """
    stack = list()
    result = list()
    stack.append(node)
    while len(stack) != 0:
        node = stack.pop()
        result.append(node.data)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    print(result[::-1])


from queue import Queue


def level_order_traversal(node):
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)


if __name__ == '__main__':
    data_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4]
    root = create_binary_tree(data_list)
    print('前序遍历: ')
    pre_order_traversal_with_stack(root)
    # pre_order_traversal(root)
    print('中序遍历: ')
    in_order_traversal_with_stack(root)
    # in_order_traversal(root)
    print('后序遍历: ')
    # post_order_traversal(root)
    post_order_traversal_with_satck(root)
    # print(f'广度遍历: {level_order_traversal(root)}')
    level_order_traversal(root)
