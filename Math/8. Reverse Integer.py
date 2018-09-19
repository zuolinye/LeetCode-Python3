# -*- coding: utf-8 -*-

"""

边界条件：
1. 输入有空格，丢弃空格
2. 字符串首位可能会有正负号
3. 第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
4. 结果太大或者太小超过int限制就要返回特定数字 2147483647 或者 -2147483648
5. 根据之前的正负号结果返回对应数值

"""
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        str =str.strip()
        strNum = 0
        # 判断去除空格后是否为空字符串
        if len(str) == 0:
            return strNum

        positive = True
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                positive = False
            str = str[1:]

        for char in str:
            if char >= '0' and char <= '9':
                strNum = strNum * 10 + ord(char) - ord('0')
            if char < '0' or char > '9':
                break

        if strNum > 2147483647:
            if positive == False:
                return -2147483648
            else:
                return 2147483647
        if not positive:
            strNum = 0 - strNum
        return strNum


if __name__ == "__main__":

    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
