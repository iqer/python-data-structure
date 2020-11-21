class Solution:

    def quick_sort(self, start_index, end_index, array):
        if start_index >= end_index:
            return
        pivot_index = self.partition_v1(start_index, end_index, array)
        self.quick_sort(start_index, pivot_index-1, array)
        self.quick_sort(pivot_index+1, end_index, array)

    def partition_v1(self, start_index, end_index, array):
        pivot = array[start_index]
        left = start_index
        right = end_index
        while left != right:
            while left < right and array[right] > pivot:
                right -= 1
            while left < right and array[left] <= pivot:
                left += 1
            if left < right:
                array[left], array[right] = array[right], array[left]

        array[start_index] = array[left]
        array[left] = pivot
        return left


if __name__ == '__main__':
    s1 = Solution()
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1.quick_sort(0, len(my_array)-1, my_array)
    print(my_array)
