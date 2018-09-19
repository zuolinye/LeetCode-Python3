class Solution():
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 如果是负数，我们需要注意转化为绝对值
        if x < 0:
            y = -1 * int(str(-x)[::-1])

        else:
            y = int(str(x)[::-1])

        if y > 2147483647 or y < -2147483647:
            y =0
        else:
            return y


if __name__ == "__main__":

    print(Solution().reverse(123))
    print(Solution().reverse(-321))
