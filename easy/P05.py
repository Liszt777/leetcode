# 罗马数字转整数   （见P04）

#  O(n) O(1)
class Solution:
    def romanToInt(self, s):
        # 初始化了一个一一对应的map，方便后面取出符号。
        lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        len_s = len(s)
        for i in range(len_s):
            # 判断左边的值是否比右边的小，并防止下标越界
            if i < len_s-1 and lookup[s[i]] < lookup[s[i+1]] :
                # 如果左边值小于右边，则减去
                res -= lookup[s[i]]
            else:
                res += lookup[s[i]]
        return res


if __name__ == '__main__':
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))
