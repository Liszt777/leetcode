# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
# 输入: 121
# 输出: true
#
# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 0(n) 0(n)
class Solution1:
    def isPalindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        return x == int(str(x)[::-1])


# 进阶:你能不将整数转为字符串来解决这个问题吗？
# O(1) O(1)
class Solution2:
    def isPalindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        res, cp_x = 0, x
        while x:
            res = res*10 + x%10
            x //= 10
        return res == cp_x


if __name__ == '__main__':
    s = Solution2()
    print(s.isPalindrome(10))
    print(s.isPalindrome(-123))
    print(s.isPalindrome(12321))

