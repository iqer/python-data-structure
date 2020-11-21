class Solution:

    def bubble_sort_2(self, array):
        for i in range(len(array)-1):
            is_sorted = True
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    is_sorted = False
            if is_sorted:
                break


if __name__ == '__main__':
    s1 = Solution()
    my_list = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1.bubble_sort_2(my_list)
    print(my_list)
