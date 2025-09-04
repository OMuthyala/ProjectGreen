# First attempt: Pretty solid solution
# Time complexity: O(1)
#   Why? Since the strings are restricted to english words, there are only 26 possible entries in the long term. So access and insert to a dict is O(1) 
# Size complexity: O(1)
#   Why? Created a dict using at most 26 elements, constant in the long term
# Method:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = dict()
        for i in s:
            if i in sdict.keys():
                sdict[i] += 1
            else:
                sdict[i] = 1
        for i in t:
            if i not in sdict.keys():
                return False
            sdict[i] -= 1
        
        for i in sdict.keys():
            if sdict[i] != 0:
                return False
        return True

# Reasoning: By creating a dict with number values, we can see the number of times each letter is used in the first word. 
#   We immediately disqualify any words that are not equal in length. By checking the ending values, if any letters are leftover, return False
# 

# More optimal solution: 
# Time complexity: 
#   Why? 
# Space complexity: 
#   Why? 
# Method:


    
# Reasoning: 
# 