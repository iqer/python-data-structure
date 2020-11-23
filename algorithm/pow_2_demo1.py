class Solution:

    def is_power_of_2_v3(self, num):
        return (num & 1) == 0


if __name__ == '__main__':
    s1 = Solution()
    print(s1.is_power_of_2_v3(2))
