from typing import List
class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        busy_count = sum(
            start <= queryTime <= end
            for start, end in zip(startTime, endTime)
        )
        return busy_count

startTime = list(map(int, input("Enter start times: ").split()))
endTime = list(map(int, input("Enter end times: ").split()))
queryTime = int(input("Enter query time: "))
sol = Solution()
print(sol.busyStudent(startTime, endTime, queryTime))