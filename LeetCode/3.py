class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandy = max(candies)
        return [candy + extraCandies >= maxCandy for candy in candies]
    
candies = list(map(int, input("Enter candies: ").split()))
extraCandies = int(input("Enter extraCandies: "))
sol = Solution()
result = sol.kidsWithCandies(candies, extraCandies)
print(result)
