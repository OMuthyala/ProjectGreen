# First submission: Not optimal but gets the job done
# Time complexity: O(nlogn)
#   Why? Sorting takes O(nlogn) and stepping through each step takes O(n) = O(n + nlogn) = O(nlogn)
# Size complexity: O(n)
#   Why? We iterate over the entire list that has already been created
# Method:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

# Reasoning: If we sort the list, then any duplicates must be next to each other in the sorted list.
#   Then by stepping through the entire list, if any 2 adjacent entires are the same, we know duplicates exist

# More optimal submission: uses set() in python
# Time complexity: O(n)
#   Why? Iterating over the given list takes O(n), at each step we add the entry to a set if its not already within the set O(1) = O(n)
# Space complexity: O(n)
#   Why? The set will at most contain every single entry in the original list, therefore O(n)
# Method:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        idk = set()
        for num in nums:
            if num in idk:
                return True
            idk.add(num)
        return False
    
# Reasoning: By creating a set, we hash every entry added to the set. If an entry is not within the set, it can be added as it is unique
#   however if the entry already exists in the set, it can be found in O(1) and the code returns True. Else False.
