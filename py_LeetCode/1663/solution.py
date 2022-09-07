class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        quotient, r = divmod(k - n, 25)
        return ("" if n == quotient else "a" * (n - quotient - 1) + chr(97 + r)) + "z" * quotient


print(Solution.getSmallestString("", 5, 130))
