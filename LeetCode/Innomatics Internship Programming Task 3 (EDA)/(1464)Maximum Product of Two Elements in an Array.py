'''Problem Link : https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/1859408521/
'''

#Code
class Solution:
  def maxProduct(self, nums: list[int]) -> int:
    max1 = 0
    max2 = 0
    for num in nums:
      if num > max1:
        max2, max1 = max1, num
      elif num > max2:
        max2 = num
    return (max1 - 1) * (max2 - 1)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
print(sol.maxProduct(nums))