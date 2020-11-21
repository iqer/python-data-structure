class Solution:

    def quick_sort(self, start_index, end_index, array):
        if start_index >= end_index:
            return
        pivot_index = self.partition_v2(start_index, end_index, array)
        # self.quick_sort(start_index, pivot_index - 1, array)
        self.quick_sort_with_stack(start_index, pivot_index - 1, array)
        # self.quick_sort(pivot_index + 1, end_index, array)
        self.quick_sort_with_stack(pivot_index + 1, end_index, array)

    def partition_v2(self, start_index, end_index, array):
        pivot = array[start_index]
        mark = start_index
        for i in range(start_index + 1, end_index + 1):
            if array[i] < pivot:
                mark += 1
                array[mark], array[i] = array[i], array[mark]
        array[start_index] = array[mark]
        array[mark] = pivot
        return mark

    def quick_sort_with_stack(self, start_index, end_index, array):
        quick_sort_stack = []
        root_param = {'startIndex': start_index, 'endIndex': end_index}
        quick_sort_stack.append(root_param)

        # 循环结束条件
        while len(quick_sort_stack) > 0:
            param = quick_sort_stack.pop()
            pivit_index = self.partition_v2(param.get('startIndex'), param.get('endIndex'), array)

            if param.get('startIndex') < pivit_index - 1:
                left_param = {'startIndex': param.get('startIndex'),
                              'endIndex': pivit_index - 1}
                quick_sort_stack.append(left_param)

            if pivit_index + 1 < param.get('endIndex'):
                right_param = {'startIndex': pivit_index + 1,
                               'endIndex': param.get('endIndex')}
                quick_sort_stack.append(right_param)


if __name__ == '__main__':
    my_array = [3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11]
    s1 = Solution()
    s1.quick_sort(0, len(my_array) - 1, my_array)
    print(my_array)
