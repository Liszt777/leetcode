# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
# 输入: 123
# 输出: 321
#
# 示例 2:
# 输入: -123
# 输出: -321
#
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回0

# O(logX) O(1)
class Solution:
    def reverse(self, x):
        """
        :param x: int
        :return: int
        """
        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            res = res*10 + x%10
            x //= 10
        return res if -pow(2, 31)<=res<=pow(2, 31)-1 else 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(99999999999999999999999999999))
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))


