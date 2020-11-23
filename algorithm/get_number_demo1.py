"""
获取最大公约数
"""

class Solution:

    def get_greatest_common_divisor_v2(self, a, b):
        big = max(a, b)
        small = min(a, b)
        if big % small == 0:
            return small
        return self.get_greatest_common_divisor_v2(big % small, small)

    def get_greatest_common_divisor_v3(self, a, b):
        if a == b:
            return a
        big = max(a, b)
        small = min(a, b)
        return self.get_greatest_common_divisor_v3(big - small, small)

    def get_greatest_common_divisor_v4(self, a, b):
        if a == b:
            return a
        if (a & 1) == 0 and (b & 1) == 0:
            return self.get_greatest_common_divisor_v4(a >> 1, b >> 1) << 1
        elif (a & 1) == 0 and (b & 1) != 0:
            return self.get_greatest_common_divisor_v4(a >> 1, b)
        elif (a & 1) != 0 and (b & 1) == 0:
            return self.get_greatest_common_divisor_v4(a, b >> 1)
        else:
            big = max(a, b)
            small = min(a, b)
            return self.get_greatest_common_divisor_v4(big - small, small)


if __name__ == '__main__':
    s1 = Solution()
    # res = s1.get_greatest_common_divisor_v2(100000, 100001)
    # res = s1.get_greatest_common_divisor_v3(100, 50)
    res = s1.get_greatest_common_divisor_v4(100000, 100001)
    print(res)
