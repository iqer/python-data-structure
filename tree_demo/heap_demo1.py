def up_adjust(array=None):
    """
    二叉堆尾节点上浮
    :param array:
    :return:
    """
    child_index = len(array) - 1
    parent_index = (child_index - 1) // 2
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        array[child_index] = array[parent_index]
        child_index = parent_index
        parent_index = (child_index - 1) // 2
    array[child_index] = temp


def down_adjust(parent_index, length, array):
    """
    二叉堆的节点下沉操作
    :param parent_index:
    :param length:
    :param array:
    :return:
    """
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and array[child_index+1] < array[child_index]:
            child_index += 1
        if temp <= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    array[parent_index] = temp


def build_heap(array):
    """
    二叉堆的构建
    :param array:
    :return:
    """
    for i in range((len(array)-2) // 2, -1, -1):
        down_adjust(i, len(array), array)


if __name__ == '__main__':
    my_array = [1, 3, 2, 6, 5, 7, 8, 9, 10, 0]
    up_adjust(my_array)
    print(my_array)
    my_array = [7, 1, 3, 10, 5, 2, 8, 9, 6]
    build_heap(my_array)
    print(my_array)
