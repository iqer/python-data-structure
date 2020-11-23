def find_lost_num(array):

    result = [0, 0]
    xor_result = 0
    for i in range(len(array)):
        xor_result ^= array[i]
    if xor_result == 0:
        raise ValueError

    separator = 1
    while 0 == (xor_result & separator):
        separator <<= 1

    for i in range(len(array)):
        if 0 == (array[i] & separator):
            result[0] ^= array[i]
        else:
            result[1] ^= array[i]
    return result


if __name__ == '__main__':
    my_array = [4, 1, 2, 2, 5, 1, 4, 3]
    print(find_lost_num(my_array))
