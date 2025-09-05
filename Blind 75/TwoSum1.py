# First submission: Probably one of the more optimal first submissions
# Time complexity: O(n)
#   Why? We iterate through the list once, at each step we check if a solution already exists = O(n)
# Size complexity: O(n)
#   Why? For each entry in the nums list, we add more info that stays O(1) = O(n)
# Method:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        coord = {}
        for i, j in enumerate(nums):
            if j in coord:
                return [coord[j], i]
            coord[target - j] = i

# Reasoning: By keeping track of the target - num value as the key and the index as the value, if there is ever an entry that
#   satisfies one of the previous element's requirements for a two-sum, we can pull the index and return the answer quickly