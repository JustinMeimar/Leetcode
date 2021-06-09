# easy difficulty; recrusive solution

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        print(n,k)
        if n == 0:
            return 0
        i = 0
        while k**i <= n/k:
            i += 1
            
        print(i)

        return 1 + self.sumBase(n-k**i,k)

k = Solution()
print(k.sumBase(68,2))
print(k.sumBase(34,6))
