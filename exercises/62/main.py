class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        r = [1] * n
        
        for i in range(m - 1):
            nr = [1] * n
            for j in range(n - 2, -1, -1):
                nr[j] = nr[j + 1] + r[j]
            r = nr
        return r[0]
