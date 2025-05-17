class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        memo={}
        def lcs(m,n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            if text1[m-1]==text2[n-1]:
                memo[(m,n)] =1+lcs(m-1,n-1)
            else:
                memo[(m,n)]=max(lcs(m,n-1), lcs(m-1,n))
            return memo[(m,n)]
        return lcs(m,n)

                

        