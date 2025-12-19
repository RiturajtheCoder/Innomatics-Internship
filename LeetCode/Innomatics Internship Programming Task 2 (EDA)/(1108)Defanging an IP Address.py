'''Problem Link : https://leetcode.com/problems/defanging-an-ip-address/submissions/1859071355/
'''

#Code
class Solution:
  def defangIPaddr(self, address: str) -> str:
    return address.replace('.', '[.]')

address = input("Enter IP address: ")
sol = Solution()
print(sol.defangIPaddr(address))