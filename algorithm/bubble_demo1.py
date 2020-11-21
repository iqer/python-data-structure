class Solution:

    def bubble_sort(self, array):
        for i in range(len(array)-1):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]


if __name__ == '__main__':
    cs = Solution()
    my_list = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    cs.bubble_sort(my_list)
    print(my_list)
