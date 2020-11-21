class Solution:

    def bubble_sort_v3(self, array):
        last_exchange_index = 0
        sort_border = len(array) - 1
        for i in range(len(array) - 1):
            is_sorted = True
            for j in range(sort_border):
                if array[j+1] < array[j]:
                    array[j+1], array[j] = array[j], array[j+1]
                    last_exchange_index = j
                    is_sorted = False
            sort_border = last_exchange_index
            if is_sorted:
                break


if __name__ == '__main__':
    s1 = Solution()
    my_list = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1.bubble_sort_v3(my_list)
    print(my_list)
