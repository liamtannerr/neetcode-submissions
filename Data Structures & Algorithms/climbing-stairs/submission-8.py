# Pattern should go 1, 2, 3, 5, 8, 13, 21 .....

# n = 5
# My algorithm: res = 5, prev = 3, prevX2 = 3, temp = 3




class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        p1 = 2
        p2 = 1
        res = p1 + p2
        for i in range(3,n):
            p2 = p1
            p1 = res
            res = p1 + p2
            print(f"n: {i}")
            print(f"res: {res}")
            print(f"#########")

        return res