class Solution:

    def cock_tail_sort_v1(self, array):

        for i in range((len(array)-1) // 2):
            is_sorted = True
            # 奇数轮
            for j in range(i, len(array)-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    is_sorted = False
            if is_sorted:
                break
            # 偶数轮
            for j in range(len(array)-i-1, i, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                    is_sorted = False
            if is_sorted:
                break


if __name__ == '__main__':
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1 = Solution()
    s1.cock_tail_sort_v1(my_array)
    print(my_array)
