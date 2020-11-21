class Solution:

    def count_sort(self, array):
        max_value = array[0]
        for i in range(1, len(array)):
            if array[i] > max_value:
                max_value = array[i]
        count_array = [0] * (max_value+1)

        for i in range(len(array)):
            count_array[array[i]] += 1

        sorted_array = list()
        for i in range(len(count_array)):
            for j in range(count_array[i]):
                sorted_array.append(i)
        return sorted_array


if __name__ == '__main__':
    my_array = [4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10]
    s1 = Solution()
    print(s1.count_sort(my_array))
