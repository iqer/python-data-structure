class Solution:

    def bucket_sort(self, array):
        max_value = array[0]
        min_value = array[0]

        for i in range(1, len(array)):
            if array[i] > max_value:
                max_value = array[i]
            if array[i] < min_value:
                min_value = array[i]

        d = max_value - min_value

        bucket_num = len(array)
        bucket_list = list()
        for i in range(bucket_num):
            bucket_list.append([])

        for i in range(len(array)):
            num = int((array[i]-min_value) * (bucket_num-1) / d)
            bucket = bucket_list[num]
            bucket.append(array[i])

        for i in range(len(bucket_list)):
            bucket_list[i].sort()

        sorted_array = list()

        for sub_list in bucket_list:
            for element in sub_list:
                sorted_array.append(element)

        return sorted_array


if __name__ == '__main__':
    my_array = [4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09]
    s1 = Solution()
    print(s1.bucket_sort(my_array))
