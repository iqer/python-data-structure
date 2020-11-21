class Solution:

    def heap_sort(self, array):
        for i in range((len(array)-2)//2, -1, -1):
            self.down_adjust(i, len(array), array)

        for i in range(len(array)-1, 0, -1):

            temp = array[i]
            array[i] = array[0]
            array[0] = temp

            self.down_adjust(0, i, array)

    def down_adjust(self, parent_index, length, array):
        temp = array[parent_index]
        child_index = 2 * parent_index + 1
        while child_index < length:
            if child_index + 1 < length and array[child_index + 1] > array[child_index]:
                child_index += 1
            if temp >= array[child_index]:
                break
            array[parent_index] = array[child_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        array[parent_index] = temp


if __name__ == '__main__':
    s1 = Solution()
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1.heap_sort(my_array)
    print(my_array)
