class Solution(object):
    def minimumTotal(self, triangle):
        minimum = len(triangle)

        for i in range(1,minimum):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
        for i in range(2,minimum):
            for j in range(1,i):
                triangle[i][j] += min(triangle[i-1][j-1:j+1])

        return min(triangle[-1])
