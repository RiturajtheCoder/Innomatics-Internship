'''Problem Link
https://leetcode.com/problems/running-sum-of-1d-array/
'''

#Code
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix =[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])

        return prefix
num=list(map(int,input().split()))
sol=Solution()
print(sol.runningSum(num))