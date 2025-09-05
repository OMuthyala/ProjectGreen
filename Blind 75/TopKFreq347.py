# First submission: Learned about this solution from a tutorial video
# Time complexity: O(nlogk)
#   Why? Since n elements need to be pushed into a heap which 
# Size complexity: O(n)
#   Why? 
# Method:

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for n, count in freq.items():
            heapq.heappush(heap, (count, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for freq, n in heap]

# Reasoning: 
# 