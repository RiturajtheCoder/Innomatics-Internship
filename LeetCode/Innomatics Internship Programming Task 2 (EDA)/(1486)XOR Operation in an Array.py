import functools
import operator

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(
            operator.xor,
            [start + 2 * i for i in range(n)]
        )

n = int(input("Enter n: "))
start = int(input("Enter start: "))
sol = Solution()
print(sol.xorOperation(n, start))
