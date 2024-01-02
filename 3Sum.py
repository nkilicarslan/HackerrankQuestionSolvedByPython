from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = {}
        res = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] not in hashmap:
                    hashmap[nums[i] + nums[j]] = [[i,j]]
                else:
                    hashmap[nums[i] + nums[j]].append([i,j])

        for index, num in enumerate(nums):
            if num > 0:
                break
            if 0 - num in hashmap:
                for candidate in hashmap[0 - num]:
                    if index not in candidate:
                        tmp = [nums[candidate[0]], nums[candidate[1]], num]
                        tmp.sort()
                        if tmp not in res:
                            res.append(tmp)
        return res

# create a test case
nums = [-1,0,1,2,-1,-4]
# instantiate the solution class
solution = Solution()
# call the function
print(solution.threeSum(nums))