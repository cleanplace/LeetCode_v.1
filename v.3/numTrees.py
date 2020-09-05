#DP
# class Solution(object):
#     def numTrees(self, n):
#
#         G = [0]*(n+1)
#         G[0], G[1] = 1, 1
#
#         for i in range(2, n+1):
#             for j in range(1, i+1):
#                 G[i] += G[j-1] * G[i-j]
#
#         return G[n]

#카탈랑 수
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)

if __name__ == "__main__":
    num = 3
    s = Solution()
    print(s.numTrees(3))