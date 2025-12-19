'''Problem Link : https://leetcode.com/problems/number-of-good-pairs/
'''

#Code
from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs_count = 0
        frequency_map = Counter()
        for num in nums:
            good_pairs_count += frequency_map[num]
            frequency_map[num] += 1
        return good_pairs_count

nums = list(map(int, input("Enter numbers separated by space: ").split()))
sol = Solution()
print(sol.numIdenticalPairs(nums))