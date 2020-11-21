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


if __name__ == '__main__':
    data_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4]
    root = create_binary_tree(data_list)
    print('前序遍历: ')
    pre_order_traversal(root)
    print('中序遍历: ')
    in_order_traversal(root)
    print('后序遍历: ')
    post_order_traversal(root)
