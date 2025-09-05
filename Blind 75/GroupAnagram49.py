# First submission: This was better than last year's submission, good stuff
# Time complexity: O(n * klogk)
#   Why? For n entries, we are sorting each word, with k chars, and placing them in a dict = O(klogk) * O(n) = O(n * klogk)
# Size complexity: O(n)
#   Why? For every word, we are storing at most one copy and one sorted version so O(2n) = O(n)
# Method:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringmap = {}
        for s in strs:
            sorts = "".join(sorted(s))
            if sorts in stringmap:
                stringmap[sorts].append(s)
            else:
                stringmap[sorts] = [s]
        return list(stringmap.values())

# Reasoning: By using the sorted version of each word, we can group anagrams by appending them to the list stored in our dict
#   an improvement on this could be to use character counts instead, as that would only take O(n * k)